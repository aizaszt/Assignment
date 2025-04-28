
import math
from shape3d import Shape3D

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

class Cube(Shape3D):
    def __init__(self, side_length):
        self.side_length = side_length

    def surface_area(self):
        return 6 * self.side_length ** 2

    def volume(self):
        return self.side_length ** 3