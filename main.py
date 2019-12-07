from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
#só descomentar se o arquivo sans-serif.tff estiver no diretorio"
#font = ImageFont.truetype("sans-serif.ttf",16)
draw.text((100,900),"Sample Text",(255,255,255))
img.save('samplee-out.jpg')
print(img.format, img.size, img.mode)
