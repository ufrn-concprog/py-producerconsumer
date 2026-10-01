"""Consumer thread implementation for the producer-consumer example."""

from buffer import SharedBuffer
from threading import Thread

class Consumer(Thread):
    """Thread that removes one item from a shared buffer."""

    def __init__(self, id, buffer):
        """Create a consumer associated with ``buffer``.

        Args:
            id: Name assigned to the thread for status messages.
            buffer: Shared buffer from which the consumer removes an item.
        """
        super().__init__()
        self.name = id
        self.buffer = buffer

    def run(self):
        """Remove one item from the shared buffer."""
        self.buffer.remove()