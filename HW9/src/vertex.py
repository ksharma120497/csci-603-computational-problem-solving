
"""
CSCI-603 Lab 9: Holi Cow!

Vertex class

author: Kapil Sharma ks4643
"""

class Vertex:
    __slots__= "_id", "_neighbors"
    _id: any
    _neighbors: dict['Vertex', int]


    def __init__(self, key):
        self._id = key
        self._neighbors = {}


    def add_neighbors(self, nbr:'Vertex', weight:int=0):
        self._neighbors[nbr] = weight

    def __str__(self):
        return str(self._id) + ' neighbors: ' + str([str(x._id) for x in self._neighbors])


    def get_neighbors(self):
        return self._neighbors.keys()


    def get_id(self):
            return self._id


    def get_weight(self, nbr: 'Vertex'):
        return self._neighbors[nbr]
