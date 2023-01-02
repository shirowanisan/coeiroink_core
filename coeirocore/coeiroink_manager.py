import glob
import json
from pathlib import Path
from typing import List, Iterable, Union

import numpy as np
import torch
import yaml
from espnet2.bin.tts_inference import Text2Speech
from espnet2.text.token_id_converter import TokenIDConverter


class MetaManager:
    @staticmethod
    def get_metas_dict() -> List[dict]:
        speaker_paths: List[str] = sorted(glob.glob('./speaker_info/**/'))

        speaker_infos = []
        for speaker_path in speaker_paths:
            with open(speaker_path + 'metas.json', encoding='utf-8') as f:
                meta = json.load(f)
            styles = [{'name': s['styleName'], 'id': s['styleId']} for s in meta['styles']]
            version = meta['version'] if 'version' in meta.keys() else '0.0.1'
            speaker_info = {
                'name': meta['speakerName'],
                'speaker_uuid': meta['speakerUuid'],
                'styles': styles,
                'version': version
            }
            speaker_infos.append(speaker_info)

        speaker_infos = sorted(speaker_infos, key=lambda x: x['styles'][0]['id'])
        return speaker_infos


class ModelManager:
    def __init__(
            self,
            config_path: Path,
            model_path: Path,
            speed_scale=1.0,
            use_gpu=False
    ):
        device = 'cuda' if use_gpu else 'cpu'
        self.tts_model = Text2Speech(
            config_path,
            model_path,
            device=device,
            seed=0,
            # Only for FastSpeech & FastSpeech2 & VITS
            speed_control_alpha=speed_scale,
            # Only for VITS
            noise_scale=0.333,
            noise_scale_dur=0.333,
        )

        with open(config_path) as f:
            config = yaml.safe_load(f)
        self.token_id_converter = TokenIDConverter(
            token_list=config["token_list"],
            unk_symbol="<unk>",
        )

    def tokens2ids(
            self,
            tokens: Iterable[str]
    ) -> np.ndarray:
        return np.array(self.token_id_converter.tokens2ids(tokens), dtype=np.int64)

    def make_voice(
            self,
            text: Union[str, torch.Tensor, np.ndarray],
            seed: int = 0
    ) -> np.ndarray:
        np.random.seed(seed)
        torch.manual_seed(seed)
        wav = self.tts_model(text)["wav"]
        wav = wav.view(-1).cpu().numpy()
        return wav

    @classmethod
    def get_character_model(
            cls,
            style_id: int,
            speed_scale: float = 1.0,
            use_gpu: bool = False
    ):
        uuid = None
        metas = MetaManager.get_metas_dict()
        for meta in metas:
            for style in meta['styles']:
                if style_id == int(style['id']):
                    uuid = meta['speaker_uuid']
        if uuid is None:
            raise Exception("Not Found Speaker Directory")

        model_folder_path = f"./speaker_info/{uuid}/model/{style_id}/"

        config_path = Path(model_folder_path + 'config.yaml')
        model_path = Path(sorted(glob.glob(model_folder_path + '*.pth'))[0])

        return ModelManager(
            config_path=config_path,
            model_path=model_path,
            speed_scale=speed_scale,
            use_gpu=use_gpu
        )
