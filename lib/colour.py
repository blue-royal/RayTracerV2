from lib.vec import *

class Colour(Vec3):
    def __init__(self, r, g, b):
        super().__init__(int(r), int(g), int(b))
        
    def __mul__(self, other):
        if type(other) == Colour:
            r = ((self.x/256) * (other.x/256)) * 256
            g = ((self.y/256) * (other.y/256)) * 256
            b = ((self.z/256) * (other.z/256)) * 256
            return Colour(r, g, b).clamp()
        else:
            return Colour(self.x*other, self.y*other, self.z*other).clamp()

    def clamp(self):
        if self.x > 255:
            self.x = 255
        elif self.x < 0:
            self.x = 0
        
        if self.y > 255:
            self.y = 255
        elif self.y < 0:
            self.y = 0
        
        if self.z > 255:
            self.z = 255
        elif self.z < 0:
            self.z = 0
        return self

    def __call__(self):
        return (self.x, self.y, self.z)

    def __repr__(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return (self.x, self.y, self.z)
    
    @staticmethod
    def max(colours):
        r = max([colour.x for colour in colours])
        g = max([colour.y for colour in colours])
        b = max([colour.z for colour in colours])
        return Colour(r, g, b)
    
    @staticmethod
    def average(colours, weights):
        r = []
        g = []
        b = []
        for i, colour in enumerate(colours):
            if weights[i] != 0:
                r.append(colour.x * weights[i])
                g.append(colour.y * weights[i])
                b.append(colour.z * weights[i])

        r = sum(r) / (len(r)*sum(weights))
        g = sum(g) / (len(g)*sum(weights))
        b = sum(b) / (len(b)*sum(weights))
        return Colour(r, g, b)