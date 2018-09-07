
from PIL import Image, ImageDraw, ImageFont

image = Image.open('msg.png')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-BoldItalic.ttf', size=16)

(x, y) = (45, 6)
color = 'red'
draw.text((x, y), name, fill=color, font=font)
image.save('msg1.png')