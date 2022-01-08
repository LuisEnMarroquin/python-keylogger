# Python keylogger

The simplest keylogger you can create using Python 3 only `keyboard` dependency

This app was created for learning and security purposes only, feel free to use it

Note: Everytime you start the app will delete logs file everytime it runs and only one instance is allowed to run at once
(this works by trying to delete the file but wont be able to because it'll used by the other instance)

## Setup and execution

All keystrokes will be saved on file `./keystrokes.log`

```shell
# Get the code from GitHub
git clone https://github.com/LuisEnMarroquin/python-keylogger.git

# Go to the project directory
cd python-keylogger/

# Install dependencies
pip install -r requirements.txt

# Run as foreground process
python keylogger.py

# Run as background process (Windows only)
pythonw keylogger.py

# Run as background process (Linux / macOS)
python keylogger.py &
```

## Stop app from logging

You can stop the background process at any time by clicking `f7` on any place, this is the easy way

The hard way is to search the process in your **Task Manager** and kill the process manually

## Linter for Python code

If you have `sh` installed you can lint all `.py` files at once by running

```shell
sh linter.sh
```

## Create portable executable

If the following fails you may need to update all your global dependencies

This will generate the executable on `dist/` folder

```shell
pyinstaller --noconsole --onefile keylogger.py
```
