from vertex import Vertex

"""
CSCI-603 Lab 9: Holi Cow!

Graph class

author: Kapil Sharma ks4643
"""

class Graph:
    __slots__ = '_vertDict', '_size'
    _vertDict: dict[int, 'Vertex']
    _size: int

    def __init__(self):
        self._vertDict = {}
        self._size = 0

    def get_vertex(self, key: int):
        if key in self._vertDict:
            return self._vertDict[key]
        else:
            return None

    def add_vertex(self, key: int, value):
        if self.get_vertex(key) is None:
            self._size += 1
            vertex = Vertex(value)
            self._vertDict[key] = vertex

    def __contains__(self, key):
        return key in self._vertDict

    def add_edge(self, source, source_value, destination, destination_value, cost=0):
        if source not in self._vertDict:
            self.add_vertex(source, source_value)
        if destination not in self._vertDict:
            self.add_vertex(destination, destination_value)
        self._vertDict[source].add_neighbors(self._vertDict[destination], cost)

    def get_vertices(self):
        return self._vertDict.keys()

    def __iter__(self):
        return iter(self._vertDict.values())

    def __str__(self):
        result = ""
        for i in self._vertDict:
            result += str(self._vertDict[i]) + "\n"
        return result

