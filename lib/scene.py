from numpy import arcsin, arctan2
from lib.settings import *
from lib.object import *
from lib.render import *
from lib.material import *

class Scene:
    def __init__(self):
        rays = []
        objects = [Sphere(Material(MELON), Vec3(0, 0.5, 3), 0.4)]
        lights = []     
        
        image = Render("tester")
           
        self.load_hdri()
           
        for i in range(HEIGHT):
            for j in range(WIDTH):
                ray = image.get_ray(i, j)
                pixel_colour = DEEP_BLUE
                for object in objects:
                    min_dist = INFINITY
                    if object.collision_dist(ray) < min_dist:
                        min_dist = object.collision_dist(ray)
                        if min_dist != INFINITY:
                            pixel_colour = object.material.colour
                if min_dist == INFINITY:
                    pixel_colour = self.miss_shader(ray)
                image.update_grid(i, j, pixel_colour)
        
        image.export()
        image.show()
        
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
        
        
