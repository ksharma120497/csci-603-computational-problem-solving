"""
CSCI-603: Trees (week 10)
Author: RIT CS

This is an implementation of a binary tree node.
"""
from typing import Any


class BST:
    __slots__='root', 'size'
    root: 'BTNode'
    size: int


    def insert_helper(self, val: None):

        if self.root is None:
            self.root = BTNode(val)
        else:
            self.insert_func(self.root, val)
        self.size+=1

    def insert_func(self, root, val):

        if root.get_value() < val:
            self.insert_func(root.get_left(), val)
        else:


class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """
    __slots__ = '_val', '_left', '_right'
    val: Any
    left: 'BTNode'
    right: 'BTNode'

    def __init__(self, val: Any, left: 'BTNode' = None, right: 'BTNode' = None) -> None:
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self._val = val
        self._left = left
        self._right = right

    def get_value(self) -> Any:
        """
        Returns the node's value
        """
        return self._val

    def get_left(self) -> 'BTNode':
        """
        Returns the left child
        """
        return self._left

    def get_right(self) -> 'BTNode':
        """
        Returns the right child
        """
        return self._right

    def set_left(self, left: 'BTNode'):
        """
        Sets the left child
        """
        self._left = left

    def set_right(self, right: 'BTNode'):
        """
        Sets the right child
        """
        self._right = right


def testBTNode() -> None:
    """
    A test function for BTNode.
    :return: None
    """
    left = BTNode(10)
    right = BTNode(20)
    parent = BTNode(30)
    parent.set_left(left)
    parent.set_right(right)
    print('parent (30):', parent.get_value())
    print('left (10):', parent.get_left().get_value())
    print('right (20):', parent.get_right().get_value())


if __name__ == '__main__':
    testBTNode()





