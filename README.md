# The Producer-Consumer Problem: A Solution in Python

This project demonstrates a bounded producer-consumer buffer using Python threads. A shared FIFO queue has a maximum capacity; producers add values and consumers remove them.

## 📝 The Producer-Consumer Problem

The producer-consumer problem uses a bounded buffer shared by producers and consumers. Producers add values to the buffer, and consumers remove them. The implementation must ensure that:

* Only one thread accesses the buffer for an insertion or removal at a time.
* Producers wait while the buffer is full.
* Consumers wait while the buffer is empty.
* Values are removed in the order they were inserted.

`SharedBuffer` in `src/buffer.py` uses `queue.Queue(maxsize=capacity)` for bounded FIFO storage. A semaphore guards queue operations. Producers wait on a condition variable while the queue is full; after inserting a value, they notify a waiting consumer. Consumers wait while the queue is empty and notify a waiting producer after removing a value. In `src/main.py`, producer-consumer pairs each handle one value, and the program joins all threads before exiting.

## 📂 Repository Structure

Source code in this repository is organized as follows:

```text
+─py-producerconsumer
  ├─── doc                  # Directory where documentation will be generated
  ├─── src                  # Directory with header files
       └─── buffer.py       # Implementatio of the shared buffer
       └─── consumer.py     # Implementation of the consumer thread
       └─── producer.py     # Implementation of the producer thread
  └─── main.py              # Main program
    
```

## 🚀 Getting Started

### ✅ Prerequisites

Python 3 is required. The program uses only the Python standard library.

### ▶️ Running

From the repository root:

```bash
python3 main.py
```

The program prints messages as values are inserted into and removed from the buffer, followed by a completion message.

## Generate Documentation

The source modules include docstrings that can be rendered with [pdoc](https://pdoc.dev). Install pdoc and generate HTML documentation from the repository root:

```bash
python3 -m pip install pdoc
python3 -m pdoc -o doc src.buffer src.consumer main src.producer
```

To serve the documentation locally instead of writing HTML files:

```bash
python3 -m pdoc src.buffer src.consumer main src.producer
```
