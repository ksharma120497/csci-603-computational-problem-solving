
class LinkedNode:
    __slots__ = ("_value", "_link")
    _value: any
    _link: 'LinkedNode'

    def __init__(self, value, link):
        self._link = link
        self._value = value

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    def get_value(self):
        return self._value



if __name__ == "__main__":
    pass


