from numpy import arcsin, arctan2
from lib.settings import *
from lib.object import *
from lib.render import *
from lib.material import *

class Scene:
    def __init__(self):
        self.objects = [Sphere(MELON, Vec3(0, 0.5, 3), 0.4), Sphere(MELON, Vec3(1, -0.5, 3), 0.6), Sphere(DEEP_BLUE, Vec3(-0.8, 00, 8), 1), Sphere(DEEP_BLUE, Vec3(0.9, 0.9, 1), 0.2)]
        self.lights = [Light(Vec3(1, 0, -1), Colour(255, 255, 255)), Light(Vec3(-1, 0, 3), Colour(255, 0, 0))]     
        
        image = Render("tester")
           
        self.load_hdri()
           
        for i in range(HEIGHT):
            for j in range(WIDTH):
                ray = image.get_ray(i, j)
                image.update_grid(i, j, self.run_ray(ray))

        image.export()
        image.show()
        
        
    
    # calculates the closest object that the ray intersects and returns its 
    # colour which is defined by its material.
    # If it misses it returns the colour of the miss shader
    def run_ray(self, ray):
        pixel_colour = DEEP_BLUE
        min_dist = INFINITY
        for object in self.objects:
            if object.collision_dist(ray) < min_dist:
                min_dist = object.collision_dist(ray)
                if min_dist != INFINITY:
                    pixel_colour = object.material.get_colour(self.lights, ray(min_dist))
        if min_dist == INFINITY:
            pixel_colour = self.miss_shader(ray)
        
        return pixel_colour
    
    def load_hdri(self):
        self.hdri = Image.open("Textures/HdrOutdoorCityPathDayClear001_JPG_4K.jpg")
        
        self.length, self.height = self.hdri.size
    
    def miss_shader(self, ray):
        # uv unwrap the image 
        u = int((0.5 + (arctan2(ray.dir.x, ray.dir.z) / (2*pi))) * self.length) % self.length
        v = (self.height - int((0.5 + (arcsin(ray.dir.y) / pi)) * self.height)) % self.height
        # sample the image
        col = self.hdri.getpixel((u, v))
        return Colour(col[0], col[1], col[2])
        
        
