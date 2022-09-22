from lib.vec import *
class Ray():
    nudge_distance = 0.01
    def __init__(self, pos, dir):
        self.dir = dir.normalise()
        self.pos = pos + (self.dir * Ray.nudge_distance)
        
    def __call__(self, t):
        return self.pos + (self.dir * t)