from buffer import SharedBuffer
from random import randint
from threading import Thread

class Producer(Thread):
    def __init__(self, id, buffer):
        super().__init__()
        self.name = id
        self.buffer = buffer
        
    def run(self):
        item = randint(1, 100)
        self.buffer.insert(item)