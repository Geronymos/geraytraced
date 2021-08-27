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

# https://stackoverflow.com/questions/48265646/rotation-of-a-vector-python

def unit_vector(vector):
    """ Returns the unit vector of the vector."""
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """Finds angle between two vectors"""
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def x_rotation(vector,theta):
    """Rotates 3-D vector around x-axis"""
    R = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0, np.sin(theta), np.cos(theta)]])
    return np.dot(R,vector)

def y_rotation(vector,theta):
    """Rotates 3-D vector around y-axis"""
    R = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(R,vector)

def z_rotation(vector,theta):
    """Rotates 3-D vector around z-axis"""
    R = np.array([[np.cos(theta), -np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]])
    return np.dot(R,vector)

class Ray:
    def __init__(self, origin3, direction3):
        # g(x): origin + x * direction
        self.origin = np.array(origin3)
        self.direction = np.array(direction3)

class Sphere:
    def __init__(self, origin3, radius1):
        # | origin + x | = radius
        self.origin = np.array(origin3)
        self.radius = radius1

player = Ray((0,0,0), (1,0,0))
sphere = Sphere((10,0,0), 4)

def shader(x,y,t):
    uv = (np.array([x,y]) / np.array(size))
    rotation = uv - 0.5

    ray = Ray(player.origin, 
            y_rotation(z_rotation(player.direction, rotation[0] * math.pi/2), rotation[1] * math.pi/2)
    )
    print(ray.direction)
    # http://kylehalladay.com/blog/tutorial/math/2013/12/24/Ray-Sphere-Intersection.html
    L = sphere.origin - ray.origin 
    tc = np.dot(L, ray.direction)

    d = np.sqrt(tc ** 2 - np.linalg.norm(L) ** 2)

    # If it is less than 0, the ray does not intersect the sphere
    result = (d > sphere.radius ) * 255
    return tuple(np.array((result, result, result), dtype='i'))
    # return tuple(np.array((ray.direction+1)/2*255, dtype='i'))
    # return tuple(np.array((*(uv*255), 0), dtype='i'))

def shader2(x,y):
    uv = (np.array([x,y]) / np.array(size)) * 255
    return tuple(np.array((*uv, 0), dtype='i'))

while True:  # main game loop
    time = pygame.time.get_ticks() / 1000
    for x in range(size[0]):
        for y in range(size[1]):
            DISPLAYSURF.set_at((x,y), shader(x,y,time))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    frame += 1
