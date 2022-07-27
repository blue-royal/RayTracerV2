from numpy import arcsin, arctan2
from settings import *
from object import *
from render import *
from material import *

class Scene:
    def __init__(self):
        rays = []
        objects = [Sphere(Material(MELON), Vec3(0, 0.5, 3), 0.4)]
        lights = []     
        
        image = Render("tester")
           
        self.loadHDRI()
           
        for i in range(HEIGHT):
            for j in range(WIDTH):
                ray = image.getRay(i, j)
                pixelColour = DEEP_BLUE
                for object in objects:
                    minDist = float("inf")
                    if object.collisionDist(ray) < minDist:
                        minDist = object.collisionDist(ray)
                        if minDist != float("inf"):
                            pixelColour = object.material.colour
                if minDist == float("inf"):
                    pixelColour = self.missShader(ray)
                image.updateGrid(i, j, pixelColour)
        
        image.export()
        image.show()
        
    def loadHDRI(self):
        self.hdri = Image.open("Textures\HdrOutdoorCityPathDayClear001_JPG_4K.jpg")
        
        self.length, self.height = self.hdri.size
    
    def missShader(self, ray):
        # uv unwrap the image 
        u = int((0.5 + (arctan2(ray.dir.x, ray.dir.z) / (2*pi))) * self.length) % self.length
        v = (self.height - int((0.5 + (arcsin(ray.dir.y) / pi)) * self.height)) % self.height
        # sample the image
        col = self.hdri.getpixel((u, v))
        return Colour(col[0], col[1], col[2])
        
        
Scene() 