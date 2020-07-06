# Python keylogger

The simplest keylogger you can create using Python 3 with only `keyboard` dependency

## Download and setup environment

```shell
https://github.com/LuisEnMarroquin/python-keylogger.git
cd python-keylogger/
pip install -r requirements.txt
```

## Run as foreground process

```shell
python klog.py
```

## Run as background process

```shell
# Windows
pythonw klog.py

# Linux
python klog.py &
```

## Stop key logging

You can stop the background process at any time by clicking `f7` on any place

## Linter

If you have `sh` installed you can lint all `.py` files at once by running

```shell
sh lint.sh
```

## Create Windows executable

If the following fails you may need to update all your global dependencies

```shell
pip install pyinstaller
pyinstaller --onefile klog.py
```

## Run at startup on Windows

```shell
python windows.py
```

To remove auto startup remove keylogger related files at:
`C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`
