from flask import Flask, request
import json
import subprocess
from subprocess import Popen
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  data = json.loads(request.data)
  os.chdir("chronograf/") # Choose the path to project root
  subprocess.call(["make", "clean"])
  subprocess.call(["git", "pull", "origin", "chrono-predix-zsse"])
  result = subprocess.call(["make"])
  if result == 0:
    name = "Build: Succeed"
    color = 'green'
  else:
    name = "Build: Failed"
    color = 'red'
  subprocess.call(["chmod", "+x", "etc/fix-folder.sh"])
  subprocess.call(["sh", "etc/fix-folder.sh"])
  Popen(["make", "run"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
  os.chdir("../")
  image = Image.open('msg.png')
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype('Roboto-BoldItalic.ttf', size=16)
  (x, y) = (45, 6)
  draw.text((x, y), name, fill=color, font=font)
  # os.chdir("/var/www") # Choose path to where you want to save output picture
  image.save('result.png')
  return "OK"

if __name__ == '__main__':
   app.run(host="localhost", port=8181)