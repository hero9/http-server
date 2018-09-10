from flask import Flask, request
import json
import subprocess
from subprocess import Popen
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  # data = json.loads(request.data)
  os.chdir("chronograf/") # Choose the path to project root
  subprocess.call(["make", "clean"])
  subprocess.call(["git", "pull", "origin", "master"]) # chrono-predix-zsse
  result = subprocess.call(["make"])
  if result == 0:
    name = "Build: Succeed"
    color = 'green'
  else:
    name = "Build: Failed"
    color = 'red'

  # subprocess.call(["chmod", "+x", "etc/fix-folder.sh"])
  # subprocess.call(["sh", "etc/fix-folder.sh"])
  os.chdir("ui/build")
  subprocess.call(["ln", "-s", "../bower_components"]) # fix fix_folder.sh script
  subprocess.call(["ln", "-s", "../static_assets"]) #fix fix_folder.sh script
  os.chdir("../../")

  Popen(["make", "run"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

  os.chdir("../") # to http-server.py location

  image = Image.open('msg.png')
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype('Roboto-BoldItalic.ttf', size=13)
  
  (x, y) = (40, 5)
  draw.text((x, y), name, fill=color, font=font)
  
  with open('chronograf/ui/package.json') as package_json:
    data = json.load(package_json)
    name = data['version']
  
  (x, y) = (110, 15)
  font = ImageFont.truetype('Roboto-BoldItalic.ttf', size=10)
  color = 'white'
  draw.text((x, y), name, fill=color, font=font)
  
  os.chdir("/var/www") # Choose path where you want to save output picture
  
  image.save('result.png')
  
  return "OK"

if __name__ == '__main__':
   app.run(host="207.154.246.33", port=8181) # type name or IP_address of your server and port