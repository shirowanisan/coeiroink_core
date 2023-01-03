# coeiroink_core

## Installation

```bash
pip install --upgrade pip setuptools wheel
pip install --no-deps -r requirements-coeiroink-no-deps.txt
pip install -r requirements-coeiroink.txt
pip install -r requirements-voicevox.txt
```

```bash
pip install git+ssh://git@github.com/shirowanisan/coeiroink_core.git
```

## Build

version: c-1.7.0+v-1.14.0

```bash
$ python --version 
Python 3.9.12
```

### Mac

```bash
pip install --upgrade pip setuptools wheel
pip install --no-deps -r requirements-coeiroink-no-deps.txt
pip install -r requirements-coeiroink.txt
pip install -r requirements-dev.txt
# if using gpu
pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
python generate_licenses.py > licenses.json
pip install pyinstaller
pyinstaller run.py
mkdir dist/run/espnet
cp venv/Lib/site-packages/espnet/version.txt dist/run/espnet/
mkdir dist/run/librosa/util/example_data
cp venv/Lib/site-packages/librosa/util/example_data/registry.txt dist/run/librosa/util/example_data/
cp venv/Lib/site-packages/librosa/util/example_data/index.json dist/run/librosa/util/example_data/
```

### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
pip list
pip install --upgrade pip setuptools wheel
pip install --no-deps -r requirements-coeiroink-no-deps.txt
pip install -r requirements-coeiroink.txt
pip install -r requirements-dev.txt
python generate_licenses.py > licenses.json
pip install pyinstaller
pyinstaller run.py
mkdir dist/run/espnet
cp venv/Lib/site-packages/espnet/version.txt dist/run/espnet/
mkdir dist/run/librosa/util/example_data
cp venv/Lib/site-packages/librosa/util/example_data/registry.txt dist/run/librosa/util/example_data/
cp venv/Lib/site-packages/librosa/util/example_data/index.json dist/run/librosa/util/example_data/
cp default.csv dist/run/
```
