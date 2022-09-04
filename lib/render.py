from math import pi, tan
from lib.settings import *
from lib.colour import *
from lib.ray import *
from PIL import Image

class Render:
    default_name = 1
    def __init__(self, image_name=str(default_name)):        
        
        self.grid = []
        for i in range(HEIGHT):
            self.grid.append([])
            for j in range(WIDTH):
                self.grid[i].append(BLACK)
        
        name = image_name
        if name == str(Render.default_name):
            Render.default_name += 1
        self.save_path = f"images/{name}.png"
    
    def get_ray(self, i, j):
        if WIDTH > HEIGHT:
            dx = (1 - (2*j/WIDTH)) * tan((FOV/360) * pi) * ASPECT_RATIO
            dy = (1 - (2*i/HEIGHT)) * tan((FOV/360) * pi)
        else:
            dx = (1 - (2*j/WIDTH)) * tan((FOV/360) * pi) 
            dy = (1 - (2*i/HEIGHT)) * tan((FOV/360) * pi) * ASPECT_RATIO
        return Ray(ORIGIN, Vec3(dx, dy, 1))

    def update_grid(self, i, j, colour):
        self.grid[i][j] = colour
    
    def export(self):
        self.image = Image.new("RGB", size = [WIDTH, HEIGHT])
        dat = []
        for row in self.grid:
            for colour in row:
                dat.append(colour())
        
        self.image.putdata(dat)
        self.image.save(self.save_path)
    
    def show(self):
        self.image.show()