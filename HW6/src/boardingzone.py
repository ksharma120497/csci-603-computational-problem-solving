import queue

class BoardingZone:
    __slots__ = ('_zone1', '_zone2', '_zone3', '_zone4')
    _zone1: queue
    _zone2: queue
    _zone3: queue
    _zone4: queue

    def __init__(self):
        self._zone1 = queue.Queue()
        self._zone2 = queue.Queue()
        self._zone3 = queue.Queue()
        self._zone4 = queue.Queue()