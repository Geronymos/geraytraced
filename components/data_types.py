import numpy as np

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