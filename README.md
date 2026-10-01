# The producer-consumer problem: A solution using semaphores and condition variables in Python

![Python](https://img.shields.io/badge/Python-3-green?logo=python)
![Build](https://img.shields.io/badge/build-manual-lightgrey)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## About

This project implements a solution to the well-known [producer-consumer](https://en.wikipedia.org/wiki/Producer–consumer_problem) problem using a semaphore and condition variables for synchronization. The condition variables enable condition-based synchronization, allowing threads to be suspended or notified for resumption of execution under specific conditions.

## 📝 The Producer-Consumer Problem

The producer-consumer problem refers to a data area (a bounded buffer) shared by two types of processes, producers and consumers. Producers generate and insert new elements into the shared buffer, while consumers remove and consume elements from it. The following constraints must also be satisfied:

* Only one operation (insertion or removal of elements into/from the buffer) can be performed at a time
* Producers cannot insert new elements when the buffer is full: they must be suspended
* Consumers cannot remove elements when the buffer is empty: they must be suspended
* Elements must be removed in the same order in which they were inserted

This solution to the problem consists of implementing the insertion and removal operations as synchronized methods, thereby ensuring their execution under mutual exclusion. While the current size of the buffer equals the established capacity, producer threads should be suspended. If it is possible to add a new element to the buffer, then a consumer thread that has been suspended should be notified to resume execution. On the other hand, while the current size of the buffer is equal to zero, consumer threads should be suspended. If it is possible to remove an element from the buffer, then a producer thread that has been suspended should be notified to resume execution.

## Repository structure

Source code in this repository is organized as follows:

```text
+─py-producerconsumer
  ├─── doc                            # Directory with HTML pages resulted from generated documentation
  └─── src                            # Directory with source code files
       └─── buffer.py                 # Implementation of the shared buffer and the synchronized operations on it
       └─── consumer.py               # Implementation of the consumer thread
       └─── main.py                   # Main program
       └─── producer.py               # Implementation of the producer thread
    
```

## 🚀 Getting Started

### ✅ Prerequisites

* Python 3
* A terminal or IDE

The program uses only Python's standard library, so no additional packages are required.

### ▶️ Running

From the project root, run:

```bash
python3 main.py
```

## 📚 Generate Documentation

The Python modules include docstrings for documentation tools such as [pdoc](https://pdoc.dev). Install pdoc and generate HTML documentation from the project root with:

```bash
python3 -m pip install pdoc
python3 -m pdoc -o doc main src.job src.printingqueue
```

## 🤝 Contributing

Contributions are welcome! Fork this repository and submit a pull request 🚀

## 📜 License

This will generate documentation for all source code files within the [`src`](src) directory into the [`doc`](doc) directory. It is also possible to render documentation live with the command

```bash
pdoc ./src
```

This command will result in opening a window in the browser running `pdoc` at a localhost server. In this case, the documentation pages will be automatically reloaded whenever changes are made to the source code.
This project is licensed under the [MIT License](LICENSE).
