# The producer-consumer problem: A solution using semaphores and condition variables in Python

## About

This project implements a solution to the well-known [producer-consumer](https://en.wikipedia.org/wiki/Producer–consumer_problem) problem using a semaphore and condition variables for synchronization. The condition variables enable condition-based synchronization, allowing threads to be suspended or notified for resumption of execution under specific conditions.

## The producer-consumer problem

The producer-consumer problem refers to a data area (a bounded buffer) shared by two types of processes, producers and consumers. Producers generate and insert new elements into the shared buffer, while consumers remove and consume elements from it. The following constraints must also be satisfied:

* Only one operation (insertion or removal of elements into/from the buffer) can be performed at a time
* Producers cannot insert new elements when the buffer is full: they must be suspended
* Consumers cannot remove elements when the buffer is empty: they must be suspended
* Elements must be removed in the same order in which they were inserted

This solution to the problem consists of implementing the insertion and removal operations as synchronized methods, thereby ensuring their execution under mutual exclusion. While the current size of the buffer equals the established capacity, producer threads should be suspended. If it is possible to add a new element to the buffer, then a consumer thread that has been suspended should be notified to resume execution. On the other hand, while the current size of the buffer is equal to zero, consumer threads should be suspended. If it is possible to remove an element from the buffer, then a producer thread that has been suspended should be notified to resume execution.

## Repository structure

Source code in this repository is organized as follows:

```
+─py-producerconsumer                 ---> Project directory
  ├─── doc                            ---> Directory with HTML pages resulting from the generated documentation
  └─── src                            ---> Directory with source code files
       └─── buffer.py                 ---> Implementation of the shared buffer and the synchronized operations on it
       └─── consumer.py               ---> Implementation of the consumer thread
       └─── main.py                   ---> Main program
       └─── producer.py               ---> Implementation of the producer thread
    
```

## Requirements

For compiling and executing the program, the following elements must be properly installed on the development environment:

* [Git](https://git-scm.com), as control version system
* [Python 3+](https://www.python.org)
* [pdoc](https://pdoc.dev), for automatic documentation generation

## Download, compilation, and execution

In the operating system’s terminal, insert the following commands to download the implementation from this Git repository and navigate to the resulting directory:

```bash
 # Download from the Git repository
 git clone https://github.com/ufrn-concprog/py-producerconsumer
 
 # Navigation to the directory
 cd py-producerconsumer
```

To run the program, insert the following command in the operating system's terminal:

```bash
python3 src/main.py
```

## Automatic generation

The generation and visualization of documentation is provided by [pdoc](https://pdoc.dev). To render documentation as HTML pages, insert the following command in the operating system's terminal:

```bash
pdoc ./src -o ./doc
```

This will generate documentation for all source code files within the [`src`](src) directory into the [`doc`](doc) directory. It is also possible to render documentation live with the command

```bash
pdoc ./src
```

This command will result in opening a window in the browser running `pdoc` at a localhost server. In this case, the documentation pages will be automatically reloaded whenever changes are made to the source code.
