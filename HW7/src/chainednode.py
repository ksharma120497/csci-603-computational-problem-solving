

"""
CSCI-603 Lab 7: LinkedHashTable

This program is for chained node definition

author: Kapil Sharma ks4643
"""
class ChainedNode:
    __slots__ = ("obj", "prev", "fwd", "next")
    obj: any
    next: 'ChainedNode'
    fwd: 'ChainedNode'
    prev: 'ChainedNode'

    def __init__(self, obj: any, prev: 'ChainedNode' = None, next: 'ChainedNode' = None, fwd: 'ChainedNode' = None):
        self.next = next
        self.prev = prev
        self.obj = obj
        self.fwd = fwd

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, next):
        self.next = next

    def get_value(self):
        return self.obj

    def __str__(self):
        result = "[ "
        n = self
        while n is not None:
            result+= str(n.obj) +"->"
            n = n.fwd
        result += " ]"
        return result

    def __repr__(self):
        result = ""
        head = self
        while head is not None:
            result += str(head.obj) + "->"
            head = head.next
        return result


if __name__ == "__main__":
    pass


