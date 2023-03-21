import os

import soundfile as sf

from coeirocore.coeiro_manager import AudioManager, EspnetModel


def test_generate_wav():
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    text = '今日はいい天気ですね'
    tokens = EspnetModel.text2tokens(text)
    wav = AudioManager().synthesis(tokens, style_id=0)
    sf.write(f"{output_dir}/output.wav", wav, 44100, 'PCM_16')
