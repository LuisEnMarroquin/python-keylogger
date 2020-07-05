# Python keylogger

The simplest keylogger you can create using Python 3 with only 1 dependency

## Download and setup environment

```shell
https://github.com/LuisEnMarroquin/python-keylogger.git
cd python-keylogger/
pip install -r requirements.txt
```

## Run as background process

Windows

```powershell
pythonw .\keylogger.py
```

Linux

```shell
python keylogger.py &
```

## Stop key logging

You can stop the background process at any time by clicking `f7`

## Create Windows executable

If the following fails you may need to update all your global dependencies

```shell
pip install pyinstaller
pyinstaller --onefile keylogger.py
```



C:\Users\Chimney\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
