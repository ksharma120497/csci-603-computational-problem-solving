""" 
file: tests.py
description: Verify the LinkedHashSet class implementation
"""

__author__ = "Kapil Sharma"

from linkedhashset import LinkedHashSet


def print_set(a_set):
    for word in a_set:  # uses the iter method
        print(word, end=" ")
    print()


def test0():
    """
    Addition functionality
    """
    table = LinkedHashSet(7)
    table.add("to")
    table.add("do")
    table.add("is")
    table.add("to")
    table.add("be")

    print_set(table)

    print("'to' in table?", table.contains("to"))
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_set(table)

def test1():
    """
    Remove functionality
    :return:
    """
    table = LinkedHashSet(100)
    table.add("batman")
    table.add("has")
    table.add("lot")
    table.add("of")
    table.add("gizmos")
    table.add("to")
    table.add("is")
    table.add("has")
    table.remove("batman")
    table.remove("has")
    table.remove("of")
    table.remove("gizmos")
    print(table)

def test2():
    """
    This test case check whether the insertion order is maintained
    :return:
    """
    table = LinkedHashSet(10)
    table.add("batman")
    table.add("has")
    table.add("lot")
    table.add("of")
    table.add("gizmos")

    head = table.front
    while head is not None:
        print(head.obj)
        head = head.next

def test3():
    """
    This test case check whether the insertion order is maintained in reverse
    :return:
    """
    table = LinkedHashSet(10)
    table.add("batman")
    table.add("has")
    table.add("lot")
    table.add("of")
    table.add("gizmos")

    head = table.back
    while head is not None:
        print(head.obj)
        head = head.prev



if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test3()
