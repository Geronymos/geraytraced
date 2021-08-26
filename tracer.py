from PIL import Image
import math

size = (100, 100)

def shader(x,y):
    r = int(math.sin(x)*255)
    return (r,r,r)

def newImg():
    img = Image.new('RGB', size)
    for x in range(size[0]):
        for y in range(size[1]):
            img.putpixel((x,y), shader(x,y))

    return img

wallpaper = newImg()
wallpaper.show()