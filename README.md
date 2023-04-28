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

version: c-1.7.3+v-1.14.5

```bash
$ python --version 
Python 3.9.12
```

### Mac

```bash
# voicevox engine
git clone git@github.com:shirowanisan/voicevox_engine.git
cd voicevox_engine
git checkout c-1.7.3+v-0.14.5
python3 -m venv venv
source ./venv/bin/activate.fish
# coeiroinkcore
pip install git+https://git@github.com/shirowanisan/espnet@espnet-0.10.3 --no-deps
pip install -r requirements.txt --no-deps
pip install .
# voicevox engine
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
cp -r ../speaker_info ./
cp -r ../open_jtalk_dic_utf_8-1.11 venv/lib/python3.9/site-packages/pyopenjtalk/open_jtalk_dic_utf_8-1.11
python run.py
# license
pip install pip-licenses
python generate_licenses.py > licenses.json
# build
pip install pyinstaller
pyinstaller run.py
# cp
mkdir -p dist/run/espnet/
cp venv/lib/python3.9/site-packages/espnet/version.txt dist/run/espnet/
mkdir -p dist/run/librosa/util/example_data
cp venv/lib/python3.9/site-packages/librosa/util/example_data/registry.txt dist/run/librosa/util/example_data/
cp venv/lib/python3.9/site-packages/librosa/util/example_data/index.json dist/run/librosa/util/example_data/
cp -r venv/lib/python3.9/site-packages/pyopenjtalk/open_jtalk_dic_utf_8-1.11 dist/run/pyopenjtalk/
cp engine_manifest.json dist/run/
cp -r engine_manifest_assets dist/run/
cp -r speaker_info dist/run/
cp default_setting.yml dist/run/
cp default.csv dist/run/
cp -r ui_template dist/run/
# test
cd dist/run/
python -c "import pyopenjtalk; pyopenjtalk.create_user_dict('default.csv','user.dic')"
./run
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
