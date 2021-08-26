#!/bin/python

from PIL import Image
import numpy as np
import math

size = (100, 100)

def shader(x,y):
    uv = (np.array([x,y]) / np.array(size))
    wave = np.sin(uv * 10)
    result = wave * 255
    return tuple(np.array((*result,0), dtype='i'))

def newImg():
    img = Image.new('RGB', size)
    for x in range(size[0]):
        for y in range(size[1]):
            img.putpixel((x,y), shader(x,y))

    return img

wallpaper = newImg()
wallpaper.show()