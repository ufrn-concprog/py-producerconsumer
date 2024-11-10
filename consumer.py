from buffer import SharedBuffer
from threading import Thread

class Consumer(Thread):
    def __init__(self, id, buffer):
        super().__init__()
        self.name = id
        self.buffer = buffer

    def run(self):
        self.buffer.remove()