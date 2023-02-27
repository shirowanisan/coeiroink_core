import os

import soundfile as sf

from coeirocore.coeiro_manager import AudioManager

if __name__ == '__main__':
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    wav = AudioManager().synthesis('こんにちは', style_id=0)
    sf.write(f"{output_dir}/output.wav", wav, 44100, 'PCM_16')
