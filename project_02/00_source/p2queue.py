"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1:
Partner 2:
Date:
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        return

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        return

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        return None
