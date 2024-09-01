
"""
CSCI-603 Lab 9: Holi Cow!

Cow Class

author: Kapil Sharma ks4643
"""

class Cow:
    __slots__ = "name", "x_coordinate", "y_coordinate"

    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x_coordinate = x
        self.y_coordinate = y

    def __str__(self):
        return str(self.name)