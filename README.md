# coeiroink_core

## Installation

```bash
pip install git+https://git@github.com/shirowanisan/espnet@espnet-0.10.3 --no-deps
pip install -r requirements.txt --no-deps
# dev
pip install -r requirements-dev.txt
```

```bash
pip install git+https://github.com/shirowanisan/coeiroink_core.git
```

## Build

version: c-1.7.0+v-1.14.0

```bash
$ python --version 
Python 3.9.12
```

### Mac

```bash
# coeiroinkcore
pip install --upgrade pip setuptools wheel
pip install --no-deps -r requirements-coeiroink-no-deps.txt
pip install -r requirements-coeiroink.txt
pip install .
# voicevox engine
pip install -r requirements.txt
# license
pip install pip-licenses
python generate_licenses.py > licenses.json
# build
pip install pyinstaller
pyinstaller run.py
cp venv/lib/python3.9/site-packages/espnet/version.txt dist/run/espnet/
mkdir -p dist/run/librosa/util/example_data
cp venv/lib/python3.9/site-packages/librosa/util/example_data/registry.txt dist/run/librosa/util/example_data/
cp venv/lib/python3.9/site-packages/librosa/util/example_data/index.json dist/run/librosa/util/example_data/
cp engine_manifest.json dist/run/
cp -r engine_manifest_assets dist/run/
cp -r speaker_info dist/run/
```

### Windows

```bash
# voicevox engine
python -m venv venv
.\venv\Scripts\activate
# coeiroinkcore
pip install --upgrade pip setuptools wheel
pip install --no-deps -r requirements-coeiroink-no-deps.txt
pip install -r requirements-coeiroink.txt
pip install .
# voicevox engine
pip install -r requirements.txt
# if using gpu
pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
# license
pip install pip-licenses
python generate_licenses.py > licenses.json
# build
pip install pyinstaller
pyinstaller run.py
mkdir dist/run/espnet
cp venv/Lib/site-packages/espnet/version.txt dist/run/espnet/
mkdir dist/run/librosa/util/example_data
cp venv/Lib/site-packages/librosa/util/example_data/registry.txt dist/run/librosa/util/example_data/
cp venv/Lib/site-packages/librosa/util/example_data/index.json dist/run/librosa/util/example_data/
cp engine_manifest.json dist/run/
cp -r engine_manifest_assets dist/run/
cp -r speaker_info dist/run/
```
