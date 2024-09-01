
class LinkedNode:
    _value: any
    _node: 'LinkedNode'

    def __init__(self, value, node):
        self._node = node
        self._value = value
    def get_link(self):
        return self._node

    def set_link(self, node):
        self._node = node

    def get_value(self):
        return self._value




class Stack:
    _top: LinkedNode

    def push(self, node):
        self._top = node

    def pop(self):
        if self._top is not None:
            self._top = self._top.get_link()
        else:
            print("Empty Stack")

    def peek(self):
        return self._top.get_value()

    def is_empty(self):
        return self._top == None

    def has_next(self,n):
        return n.get_link() != None

    def __str__(self):
        result = "Stack ["
        n = self._top
        while( n != None):
            result += n.get_value()
            if self.has_next(n):
                result += ","
            n = n.get_link()
        result += "]"

        return result



def main():
    s = Stack()
    s.push(LinkedNode("1" ,LinkedNode('Kapil' ,LinkedNode("12", None))))
    print(s)
    print(s.peek())
    s.pop()
    print(s.peek())

if __name__ == '__main__':
    main()
