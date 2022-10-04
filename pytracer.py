#!/bin/python

import pygame
import sys
from pygame.locals import *
import numpy as np
import math
import random
from components.vector_helper import *
from components.data_types import *

""" Global variables """
size = (400, 300)
frame = 0

""" pygame init """
pygame.init()
DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Hello World!')

""" variables for the raytracer """
player = Ray((0,0,0), (1,0,0))
sphere = Sphere((10,0,0), 4)

""" gets executed for every pixel and outputs its color """
def shader(x,y,t):
    uv = (np.array([x,y]) / np.array(size))
    rotation = uv - 0.5

    ray = Ray(player.origin, 
            y_rotation(z_rotation(player.direction, rotation[0] * math.pi/2), rotation[1] * math.pi/2)
    )

    print(ray.direction)
    
    # http://kylehalladay.com/blog/tutorial/math/2013/12/24/Ray-Sphere-Intersection.html
    """ calculate the distance between the ray and sphere origin to see if its in the radius of the sphere (intersecting) """
    L = sphere.origin - ray.origin 
    tc = np.dot(L, ray.direction)
    d = np.sqrt(tc ** 2 - np.linalg.norm(L) ** 2)
    
    result = (d > sphere.radius ) * 255
    
    return tuple(np.array((result, result, result), dtype='i'))

""" Basic shader for testing (output uv) """
def shader2(x,y):
    uv = (np.array([x,y]) / np.array(size)) * 255
    return tuple(np.array((*uv, 0), dtype='i'))

def main():
    global frame
    while True:  # main game loop
        time = pygame.time.get_ticks() / 1000

        """ loop over every pixel and execute shader """
        # random.randint(0,size[0])
        # for x in range(size[0]):
        #     for y in range(size[1]):
        #         DISPLAYSURF.set_at((x,y), shader(x,y,time))
        #     pygame.display.update()

        for _ in range(0, size[0] * size[1]):
            x = random.randint(0, size[0])
            y = random.randint(0, size[1])
            DISPLAYSURF.set_at((x,y), shader(x,y,t))
            pygame.display.update()


        """ listen for events """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        frame += 1

if __name__ == "__main__":
    main()
