from PIL import Image
from operator import itemgetter

original = Image.open("original.png","r")
edit = Image.new("RGB",(original.width,original.height))

for y in range(edit.height):
    pixels = list()
    for x in range(edit.width):
        pixels.append(original.getpixel((x,y)))
    pixels.sort(key=itemgetter(0))
    for x in range(edit.width):
        edit.putpixel((x,y),pixels.pop())

edit.save("edit.png")
