
"""
CSCI-603 Lab 9: Holi Cow!

Paintball class

author: Kapil Sharma ks4643
"""
class Paintball:
    __slots__ = "color", "x_coordinate", "y_coordinate", "radius"

    def __init__(self, color, x, y, radius):
        self.color = color
        self.x_coordinate = x
        self.y_coordinate = y
        self.radius = radius

    def __str__(self):
        return str(self.color)