from vec import Vec3
class Ray():
    def __init__(self, pos, dir):
        # self.xPix = i
        # self.yPix = j
        self.pos = pos
        self.dir = dir.normalise()
    
    def __call__(self, t):
        return self.pos + (t * self.dir)