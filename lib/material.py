from lib.ray import Ray
from lib.colour import Colour
from lib.settings import BLACK

class Material:
    def __init__(self, colour, object, is_translucent=0, refraction_index=1):
        self.albedo = colour
        self.object = object
        self.refraction_index = refraction_index
        self.reflectivity = 0.2
        self.refractivity = 0.7
        self.is_translucent = is_translucent

    def get_colour(self, lights, pos, scene, ray):
        normal = self.object.get_normal(pos)
        combined_colours = []
        combined_weights = []
        colours = []
        for light in lights:
            to_light = (light.pos - pos).normalise()
            colours.append(self.albedo*light.colour*(to_light.dot(normal)))
        albedo = Colour.max(colours)
        combined_colours.append(albedo)
        combined_weights.append(0.1)
        
        # reflection
        if (normal - ray.dir).magnitude() > 1:
            reflection = ray.dir - (normal * (2 * ray.dir.dot(normal)))
            reflection = scene.run_ray(Ray(pos, reflection))
            combined_colours.append(reflection)
            combined_weights.append(self.reflectivity)
        # refraction
        # compare with normal surface:
        if self.is_translucent:
            if (normal - ray.dir).magnitude() > 1:
                n = 1/self.refraction_index
            else:
                n = self.refraction_index/1
            cosI = abs(ray.dir.dot(normal))
            sinT2 = (n**2) * (1.0 - (cosI**2))
            if sinT2 > 1:
                return BLACK
            cosT = (1.0 - sinT2)**0.5
            refraction = (ray.dir * n) + (normal * (n * cosI - cosT))
            refraction = scene.run_ray(Ray(pos, refraction))
            combined_colours.append(refraction)
            combined_weights.append(self.refractivity)
            
        return Colour.average(combined_colours,combined_weights)
