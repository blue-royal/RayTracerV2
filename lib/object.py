from math import sqrt
from lib.settings import *

class Light():
    def __init__ (self, pos): # , intensity):
        self.pos = pos
        # self.intensity = intensity

class Entity:
    def __init__(self, material):
        self.material = material

class Sphere(Entity):
    def __init__(self, material, pos, radius):
        super().__init__(material)
        self.pos = pos
        self.radius = radius
    def collision_dist(self, ray):
        # forms a quadratic in the form ax**2 + bx + c
        b = 2 * (ray.dir.dot(ray.pos - self.pos))
        c = (ray.pos - self.pos).magnitude()**2 - self.radius**2
        discrim = (b**2) - (c * 4)
        if discrim >= 0:
            larger = (-b + sqrt(discrim)) / 2
            smaller = (-b - sqrt(discrim)) / 2
            if smaller > 0:
                return smaller
            elif larger > 0:
                return larger
        return INFINITY


