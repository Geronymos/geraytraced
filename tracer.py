#!/bin/python

from PIL import Image
import numpy as np
import math

size = (100, 100)

def shader(x,y):
    uv = (np.array([x,y]) / np.array(size))
    u, v = uv - 0.5
    circle = (math.sqrt( u **2 + v ** 2 ) > .5) * 255
    result = circle
    print(result)
    return tuple(np.array((circle, circle, circle), dtype='i'))

def newImg():
    img = Image.new('RGB', size)
    for x in range(size[0]):
        for y in range(size[1]):
            img.putpixel((x,y), shader(x,y))

    return img

wallpaper = newImg()
wallpaper.show()