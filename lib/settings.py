from lib.colour import *
WIDTH = 800
HEIGHT = 501
# SAMPLES = 1
ASPECT_RATIO = WIDTH/HEIGHT if WIDTH > HEIGHT else HEIGHT/WIDTH
FOV = 90

# sample colours
DEEP_BLUE = Colour(0, 102, 153)
MELON = Colour(247, 152, 98)
BLACK = Colour(0, 0, 0)
WHITE = Colour(255, 255, 255)

# cooridinates
ORIGIN = Vec3(0, 0, 0)

# important values
INFINITY = float("inf")