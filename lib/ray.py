from lib.vec import *
class Ray():
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir.normalise()
    
    def __call__(self, t):
        return self.pos + (self.dir * t)