@ECHO OFF

pyinstaller --noconsole --onefile klog.py
pyinstaller --noconsole --onefile startup.py

exit 0
