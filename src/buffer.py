"""Thread-safe bounded buffer used by the producer and consumer threads.

The buffer combines :class:`queue.Queue` with condition variables to suspend
producers while the buffer is full and consumers while it is empty.
"""

from queue import Queue
from threading import current_thread, Condition, Semaphore

class SharedBuffer:
    """Coordinate FIFO item exchange between producer and consumer threads.

    Args:
        capacity: Maximum number of items that may be stored at once.
    """

    def __init__(self, capacity):
        """Initialize an empty buffer with the requested capacity."""
        self.buffer = Queue(maxsize=capacity)
        self.semaphore = Semaphore(1)
        self.not_full = Condition()
        self.not_empty = Condition()

    def insert(self, item):
        """Insert ``item``, waiting until space is available.

        Args:
            item: Value to append to the buffer.
        """
        with self.not_full:
            while True:
                self.semaphore.acquire()
                if not self.buffer.full():
                    try:
                        self.buffer.put(item)
                    finally:
                        self.semaphore.release()
                    break
                self.semaphore.release()
                print(f"Buffer is full. {current_thread().name} suspended.")
                self.not_full.wait()

            print(f"{current_thread().name} inserted {item}")

        with self.not_empty:
            self.not_empty.notify()

    def remove(self):
        """Remove the oldest item, waiting if the buffer is empty."""
        with self.not_empty:
            while True:
                self.semaphore.acquire()
                if not self.buffer.empty():
                    try:
                        item = self.buffer.get()
                    finally:
                        self.semaphore.release()
                    break
                self.semaphore.release()
                # Wait until there is an item in the buffer
                print(f"Buffer is empty. {current_thread().name} suspended.")
                self.not_empty.wait()

            print(f"{current_thread().name} removed {item}")

        with self.not_full:
            self.not_full.notify()