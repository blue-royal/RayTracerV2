from lib.ray import Ray
from lib.colour import Colour
from lib.settings import BLACK

class Material:
    def __init__(self, colour, object):
        self.albedo = colour
        self.object = object
        self.reflectivity = 0.9

    def get_colour(self, lights, pos, scene, ray):
        normal = self.object.get_normal(pos)
        # colours = []
        # for light in lights:
        #     to_light = (light.pos - pos).normalise()
        #     colours.append(self.albedo*light.colour*(to_light.dot(normal)))
        # albedo = Colour.max(colours)
        
        # # reflection
        # reflection = ray.dir - (normal * (2 * ray.dir.dot(normal)))
        # reflection = scene.run_ray(Ray(pos, reflection))
        
        # refraction
        n = 1.5/1
        cosI = abs(ray.dir.dot(normal))
        sinT2 = (n**2) * (1.0 - (cosI**2))
        if sinT2 > 1:
            return BLACK
        cosT = (1.0 - sinT2)**0.5
        refraction = (ray.dir * n) + (normal * (n * cosI - cosT))
        refraction = scene.run_ray(Ray(pos, refraction))
        
        
        return refraction# Colour.average([albedo, reflection], [1 - self.reflectivity, self.reflectivity])
