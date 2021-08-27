#!/bin/python

import pygame
import sys
from pygame.locals import *
import numpy as np
import math

size = (400, 300)
frame = 0

pygame.init()
DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Hello World!')

def shader(x,y,t):
    uv = (np.array([x,y]) / np.array(size))
    u, v = uv - math.sin(t)
    circle = (math.sqrt( u **2 + v ** 2 ) > .5) * 255
    result = circle
    # print(result)
    return tuple(np.array((circle, circle, circle), dtype='i'))

while True:  # main game loop
    time = pygame.time.get_ticks() / 1000
    for x in range(size[0]):
        for y in range(size[1]):
            DISPLAYSURF.set_at((x,y), shader(x,y,frame/100))

    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
    pygame.display.update()
    frame += 1
