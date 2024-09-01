import linkednode

class Queue:
    __slots__ = ("_front", "_rear")
    _front: 'linkednode'
    _rear: 'linkednode'


    def __init__(self):
        self._front = None
        self._rear = None
    def enqueue(self, value):
        node = linkednode.LinkedNode(value, None)
        if self._front == None:
            self._front = node
        else:
            self._rear.set_link(node)
        self._rear = node

    def dequeue(self):
        assert not self.is_empty(), "Dequeue from empty stack"
        self._front = self._front.get_link()
        if self._front == None:
            self._rear = None

    def peek(self):
        assert not self.is_empty(), "peek from empty queue"
        return self._front.get_value()

    def is_empty(self):
        return self._front == None

    def length(self):
        count = 0
        head = self._front
        while head:
            head = head.get_link()
            count+=1
        return count

    def __str__(self):
        result = "Queue ["
        n = self._front
        while n != None:
            result += " " + str(n.get_value())
            n = n.get_link()
            result += "]"
        return result