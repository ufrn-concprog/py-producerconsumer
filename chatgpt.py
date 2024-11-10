from queue import Queue
from threading import Thread, current_thread, Condition, Semaphore
import time

class SharedBuffer:
    def __init__(self, capacity):
        self.buffer = Queue(maxsize=capacity)
        self.semaphore = Semaphore(1)          # Semaphore for mutual exclusion (one thread at a time)
        self.not_full = Condition()           # Condition for when the buffer is not full
        self.not_empty = Condition()          # Condition for when the buffer is not empty
        self.total_items = 0                  # Track total items produced
        self.max_items = 15                   # Max items to be produced/consumed (adjust as needed)
        self.produced = 0                     # Track the number of items produced
        self.consumed = 0                     # Track the number of items consumed

    def insert(self, item):
        with self.not_full:  # Acquire the lock before checking the buffer state
            while self.buffer.full():
                print(f"Buffer is full. {current_thread().name} suspended.")
                self.not_full.wait()  # Wait until there's space in the buffer

            # Now that there's space, acquire the semaphore before modifying the buffer
            with self.semaphore:
                self.buffer.put(item)
                print(f"{current_thread().name} inserted {item}")
                self.produced += 1  # Increment the number of items produced

            # Notify consumers that the buffer is no longer empty
            with self.not_empty:
                self.not_empty.notify()

    def remove(self):
        with self.not_empty:  # Acquire the lock before checking the buffer state
            while self.buffer.empty():
                print(f"Buffer is empty. {current_thread().name} suspended.")
                self.not_empty.wait()  # Wait until there's an item to consume

            # Now that there is an item, acquire the semaphore before modifying the buffer
            with self.semaphore:
                item = self.buffer.get()
                print(f"{current_thread().name} removed {item}")
                self.consumed += 1  # Increment the number of items consumed

            # Notify producers that the buffer is no longer full
            with self.not_full:
                self.not_full.notify()

        return item

    def is_done(self):
        # Check if all items have been produced and consumed
        return self.produced >= self.max_items and self.consumed >= self.max_items

# Producer and consumer thread functions
def producer(buffer, item):
    buffer.insert(item)

def consumer(buffer):
    buffer.remove()

if __name__ == "__main__":
    capacity = 3
    buffer = SharedBuffer(capacity)

    # Create producer and consumer threads
    producers = [Thread(target=producer, args=(buffer, f"Item-{i}"), name=f"Producer-{i}") for i in range(5)]
    consumers = [Thread(target=consumer, args=(buffer,), name=f"Consumer-{i}") for i in range(5)]

    # Start all producer and consumer threads
    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    # Wait for producers to finish producing
    for p in producers:
        p.join()

    # Wait for consumers to finish consuming
    for c in consumers:
        c.join()

    # Check if all production and consumption is done
    if buffer.is_done():
        print("All production and consumption done.")
    else:
        print("Not all items were produced or consumed.")
