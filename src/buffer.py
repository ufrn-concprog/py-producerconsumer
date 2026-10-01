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
        self.semaphore = Semaphore()
        self.not_full = Condition()     # Condition variable for buffer not full
        self.not_empty = Condition()    # Condition variable for buffer not empty

    def insert(self, item):
        """Insert ``item``, waiting until space is available.

        Args:
            item: Value to append to the buffer.
        """
        with self.not_full:
            while self.buffer.full():
                print(f"Buffer is full. {current_thread().name} suspended.")
                self.not_full.wait()

        # Acquire buffer lock to insert an item
        self.semaphore.acquire()
        self.buffer.put(item)
        print(f"{current_thread().name} inserted {item}")
        self.semaphore.release()

        # Notify consumers that there is now an item in the buffer
        with self.not_empty:
            self.not_empty.notify()
            

    def remove(self):
        """Remove the oldest item, waiting if the buffer is empty."""
        with self.not_empty:
            while self.buffer.empty():
                # Wait until there is an item in the buffer
                print(f"Buffer is empty. {current_thread().name} suspended.")
                self.not_empty.wait()

        # Acquire buffer lock to remove an item
        self.semaphore.acquire()
        item = self.buffer.get(timeout=1)
        print(f"{current_thread().name} removed {item}")
        self.semaphore.release()

        # Notify producers that there is now space in the buffer
        with self.not_full:
            self.not_full.notify()