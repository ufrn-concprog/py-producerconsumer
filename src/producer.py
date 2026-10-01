"""Producer thread implementation for the producer-consumer example."""

from buffer import SharedBuffer
from random import randint
from threading import Thread

class Producer(Thread):
    """Thread that creates and inserts one random item into a buffer."""

    def __init__(self, id, buffer):
        """Create a producer associated with ``buffer``.

        Args:
            id: Name assigned to the thread for status messages.
            buffer: Shared buffer into which the producer inserts an item.
        """
        super().__init__()
        self.name = id
        self.buffer = buffer
        
    def run(self):
        """Generate one integer from 1 to 100 and insert it into the buffer."""
        item = randint(1, 100)
        self.buffer.insert(item)