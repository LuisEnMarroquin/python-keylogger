# Python keylogger

A simple keylogger for Windows using Python 3

## Execute

```shell
cd python-keylogger/ # Move to code folder
pip install -r requirements.txt # Install dependencies
python keylogger.py & # Run in background
```

## Create Windows exe

```shell
pip install pyinstaller
pyinstaller --onefile keylogger.py
```
