"""Run a producer-consumer demonstration with five producer-consumer pairs."""

from src.buffer import SharedBuffer
from src.consumer import Consumer
from src.producer import Producer

capacity = 3
num_threads = 5

buffer = SharedBuffer(capacity)

producers = []
consumers = []
for i in range(num_threads):
    p = Producer("Producer " + str(i+1), buffer)
    c = Consumer("Consumer " + str(i+1), buffer)
    producers.append(p)
    consumers.append(c)

for i in range(num_threads):
    producers[i].start()

for i in range(num_threads):
    consumers[i].start()

for i in range(num_threads):
    producers[i].join()

for i in range(num_threads):
    consumers[i].join()

print("No more production or consumption.")
