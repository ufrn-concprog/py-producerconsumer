from queue import Queue
from threading import current_thread, Condition, Semaphore

class SharedBuffer:
    def __init__(self, capacity, no_items):
        self.buffer = Queue(maxsize=capacity)
        self.semaphore = Semaphore()
        self.not_full = Condition()     # Condition variable for buffer not full
        self.not_empty = Condition()    # Condition variable for buffer not empty
        self.no_items = no_items
        self.produced_items = 0
    

    def insert(self, item):
        with self.not_full:
            while self.buffer.full():
                print(f"Buffer is full. {current_thread().name} suspended.")
                self.not_full.wait()

            # Acquire buffer lock to insert an item
            self.semaphore.acquire()
            self.buffer.put(item)
            self.produced_items += 1
            print(f"{current_thread().name} inserted {item}")
            self.semaphore.release()

            # Notify consumers that there is now an item in the buffer
            with self.not_empty:
                self.not_empty.notify()


    def remove(self):
        with self.not_empty:
            while self.buffer.empty():
                # Wait until there is an item in the buffer
                print(f"Buffer is empty. {current_thread().name} suspended.")
                self.not_empty.wait()

            # Acquire buffer lock to remove an item
            self.semaphore.acquire()
            item = self.buffer.get()
            print(f"{current_thread().name} removed {item}")
            self.semaphore.release()

            # Notify producers that there is now space in the buffer
            with self.not_full:
                self.not_full.notify()

    def is_done(self):
        return self.produced_items == self.no_items