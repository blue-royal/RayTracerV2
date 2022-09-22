from math import sqrt
from lib.material import Material
from lib.settings import *

class Light():
    def __init__ (self, pos, colour): # , intensity):
        self.pos = pos
        self.colour = colour
        # self.intensity = intensity

class Entity:
    def __init__(self, material, pos):
        self.material = material
        self.pos = pos

class Sphere(Entity):
    def __init__(self, colour, pos, radius, is_translucent=0, refraction_index=1):
        material = Material(colour, self, is_translucent, refraction_index)
        super().__init__(material, pos)
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

    def get_normal(self, pos):
        return (pos - self.pos).normalise()

