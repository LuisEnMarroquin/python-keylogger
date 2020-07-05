# Python keylogger

The simplest keylogger you can create using Python 3 with only 1 dependency

## Download and setup environment

```shell
https://github.com/LuisEnMarroquin/python-keylogger.git
cd python-keylogger/
pip install -r requirements.txt
```

## Run as foreground process

```shell
python keylogger.py
```

## Run as background process

```shell
# Windows
pythonw keylogger.py

# Linux
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

## Run at startup on Windows

```shell
python windows.py
```

To remove auto startup remove keylogger related files at:
`C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`
