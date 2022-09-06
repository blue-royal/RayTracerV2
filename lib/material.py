from .colour import Colour


class Material:
    def __init__(self, colour, object):
        self.albedo = colour
        self.object = object

    def get_colour(self, lights, pos):
        normal = self.object.get_normal(pos)
        colours = []
        for light in lights:
            to_light = (light.pos - pos).normalise()
            colours.append(self.albedo*light.colour*(to_light.dot(normal)))
        return Colour.max(colours)
