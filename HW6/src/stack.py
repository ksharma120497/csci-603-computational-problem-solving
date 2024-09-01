import linkednode

class Stack:
    __slots__ = "_top"
    _top: 'linkednode'

    def __init__(self):
        self._top = None

    def push(self, value):
        self._top = linkednode.LinkedNode(value, self._top)

    def pop(self):
        self._top = self._top.get_link()

    def peek(self):
        return self._top.get_value()

    def is_empty(self):
        return self._top == None

    def length(self):
        count = 0
        head = self._top
        while head:
            head = head.get_link()
            count += 1
        return count


    def __str__(self):
        result = ""
        n = self._top
        while n!=None:
            if n.get_link() is not None:
                result+=str(n.get_value()) + "\n\t "
            else:
                result+=str(n.get_value())
            n=n.get_link()
        return result

    def reverse(self):
        stack = Stack()
        node = self._top
        while node != None:
            stack.push(node.get_value())
            node = node.get_link()
        return stack



