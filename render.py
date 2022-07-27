from math import pi, tan
from settings import *
from colour import *
from ray import *
from PIL import Image

class Render:
    defaultName = 1
    def __init__(self, imageName=str(defaultName)):        
        
        self.grid = []
        for i in range(HEIGHT):
            self.grid.append([])
            for j in range(WIDTH):
                self.grid[i].append(BLACK)
        
        name = imageName
        if name == str(Render.defaultName):
            Render.defaultName += 1
        self.savePath = f"images\\{name}.png"
    
    def getRay(self, i, j):
        dx = (1 - (2*j/WIDTH)) * tan((FOV/360) * pi) * ASPECT_RATIO
        dy = (1 - (2*i/HEIGHT)) * tan((FOV/360) * pi)
        return Ray(ORIGIN, Vec3(dx, dy, 1))

    def updateGrid(self, i, j, colour):
        self.grid[i][j] = colour
    
    def export(self):
        self.image = Image.new("RGB", size = [WIDTH, HEIGHT])
        dat = []
        for row in self.grid:
            for colour in row:
                dat.append(colour())
        
        self.image.putdata(dat)
        self.image.save(self.savePath)
    
    def show(self):
        self.image.show()