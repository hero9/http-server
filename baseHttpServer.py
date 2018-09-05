from PIL import Image, ImageDraw, ImageFont
image = Image.open('msg.jpg')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Bold.ttf', size=13)
(x, y) = (50, 5)
name = 'Build: Success'
color = '#b85c00' # white color
draw.text((x, y), name, fill=color, font=font)

image.save('msg1.png')