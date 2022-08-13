from lib.vec import *
class Colour(Vec3):
    def __init__(self, r, g, b):
        super().__init__(int(r), int(g), int(b))
        
    def __call__(self):
        return (self.x, self.y, self.z)
    def __repr__(self):
        return (self.x, self.y, self.z)
    def __str__(self):
        return (self.x, self.y, self.z)