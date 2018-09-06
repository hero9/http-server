from flask import Flask, request
import json
import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  data = json.loads(request.data)
  if data:
    print ("hello")
    bashCommand = """
    if git clone https://github.com/influxdata/chronof.git ; then
        echo "succeeded"
    else
        echo "failed"
    fi
    """
    os.system(bashCommand)
    os.chdir("git/http-server")
    subprocess.call(["git", "pull", "origin", "master"])
    os.chdir("../../") 
    image = Image.open('msg.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=13)
    (x, y) = (50, 5)
    name = "Build: Succeed"
    color = '#b85c00'
    draw.text((x, y), name, fill=color, font=font)
    os.chdir("/var/www")
    image.save('msg1.png')
    return "OK"
  return "NOT OK"

if __name__ == '__main__':
   app.run(host="207.154.246.33", port=8888)