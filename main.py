import os

import soundfile as sf

from coeirocore.coeiroink_manager import EspnetModel

if __name__ == '__main__':
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    wav = EspnetModel.get_character_model(style_id=1).make_voice('こんにちは')
    sf.write(f"{output_dir}/output.wav", wav, 44100, 'PCM_16')