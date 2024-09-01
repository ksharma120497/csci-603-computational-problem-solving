class TreeNode:
    __slots__ = 'val', 'children', 'parent'

    def __init__(self, val, parent=None):
        self.val = val
        self.children = []
        self.parent = parent

    def getStringRep(self):  # do not modify
        return self._getStringRep(0)

    def _getStringRep(self, depth):  # do not modify
        ret = self.val
        for c in self.children:
            ret += "\n" + "    " * depth + "x---" + (c._getStringRep(depth + 1))
        return ret

    def __str__(self):  # do not modify
        return str(self.val)

    def __repr__(self):  # do not modify
        return str(self.val)

    def __eq__(self, other):  # do not modify
        if type(self) != type(other):
            return False
        return self.val == other.val


class Tree:
    __slots__ = 'root', 'nodeLookup'

    def __init__(self):  # do not modify
        self.root = None
        self.nodeLookup = dict()

    def getStringRep(self):  # do not modify
        if self.root:
            return self.root.getStringRep()
        return "[empty]"

    def getNodeByValue(self, value):  # do not modify
        return self.nodeLookup[value]

    def addRoot(self, value):  # do not modify
        """
          Creates a new node using the value and places it at the root
          :param value: the value of the root
          """
        assert value not in self.nodeLookup and not self.root
        assert type(value) == str
        node = TreeNode(value)
        self.nodeLookup[value] = node
        self.root = node

    def addChildTo(self, newChildValue, parentValue):
        """
          Creates a new node using the newChildValue and adds it to the node representing the parentValue
          :param newChildValue: The value of the new child node
          :param parentValue: The value of the intended parent

          """

        assert parentValue in self.nodeLookup and newChildValue not in self.nodeLookup
        assert type(newChildValue) == str and type(parentValue) == str
        node = TreeNode(newChildValue, parentValue)
        parentNode = self.getNodeByValue(parentValue)
        parentNode.children.append(node)
        self.nodeLookup[newChildValue] = node

    def getHeight(self):
        """ Calculates the height of the tree"""
        if self.root is None:
             return -1
        elif len(self.root.children)==0:
             return 0
        else:
             return self.__getHeightHelper(self.root.val)

    def __getHeightHelper(self, root):
         if len(root) == 0:
              return -1
         node = self.getNodeByValue(root)
         height = 0
         # while len(node.children) > 0:
         #      l = node.children
         #      max = 0
         #      for i in range(len(l)):
         #           if len(l[i].children) > max:
         #                node = l[i]
         #      height+=1
         return height

    def getPathToAncestor(self, nodeValue, ancValue):
        """
           Finds the path (if it exists) between the node specified by nodeValue and the ancestor node specified by ancValue
          :param nodeValue: The value of the node
          :param ancValue: The value of the ancestor node
          :return: A list of nodes representing the path between the node and its ancestor or an empty list if the ancestor node given is not actually an ancestor
          """
        assert nodeValue in self.nodeLookup and ancValue in self.nodeLookup
        assert type(nodeValue) == str and type(ancValue) == str
        node = self.getNodeByValue(nodeValue)
        l=[node.val]
        while node.val != ancValue:
             l.append(node.parent)
             node = self.getNodeByValue(node.parent)
        return l



def test():
    t = Tree()
    t.addRoot("thing")
    # add children here
    t.addChildTo("animal", "thing")
    # add the rest here
    t.addChildTo("plant", "thing")
    t.addChildTo("mammal", "animal")
    t.addChildTo("fish","animal")
    t.addChildTo("dog", "mammal")
    t.addChildTo("cat", "mammal")
    t.addChildTo("human", "mammal")
    t.addChildTo("tuna", "fish")

    print(t.getStringRep())
    # # height
    print(t.getHeight())

    print("getPathToAncestor('animal','thing') =", t.getPathToAncestor('animal', 'thing'))
    print("getPathToAncestor('dog','mammal') =", t.getPathToAncestor('dog', 'mammal'))
    print("getPathToAncestor('dog','animal') =", t.getPathToAncestor('dog', 'animal'))



if __name__ == '__main__':
    test()
