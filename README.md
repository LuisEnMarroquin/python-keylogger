# Python keylogger

The simplest keylogger you can create using Python 3 only `keyboard` dependency

This app was created for learning and security purposes only, feel free to use it

Note: Everytime you start the app will delete logs file everytime it runs and only one instance is allowed to run at once
(this works by trying to delete the file but wont be able to because it'll used by the other instance)

## Download and install dependencies

```shell
git clone https://github.com/LuisEnMarroquin/python-keylogger.git
cd python-keylogger/
pip install -r requirements.txt
```

Note: Remember to change the url where data is posted to avoid sending me your keystrokes

## Run as foreground process

```shell
python keylogger.py
```

## Run as background process

```shell
# Windows
pythonw keylogger.py

# Linux / macOS
python keylogger.py &
```

## Key logging file

All keystrokes are saved at `~/keystrokes.log`

```shell
cat ~/keystrokes.log
```

## Stop key logging

You can stop the background process at any time by clicking `f7` on any place, this is the easy way

The hard way is to search the process in your **Task Manager** and kill the process manually

## Linter

If you have `sh` installed you can lint all `.py` files at once by running

```shell
sh linter.sh
```

## Create Windows executable

If the following fails you may need to update all your global dependencies

```shell
pip install pyinstaller
pyinstaller --noconsole --onefile keylogger.py
```

## Create portable executable for Windows

This will generate the `exe` file in `dist/` folder

```shell
pyinstaller --noconsole --onefile keylogger.py
```
