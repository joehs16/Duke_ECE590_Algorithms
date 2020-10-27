"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1: Joseph Hsieh
Partner 2: Sutianyi Wen
Date: 10/23/2020
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
        #compares the elements in the array to the length of the array
        if self.numElems == len(self.queue):
            return True
        else:
            return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        if self.numElems == 0:
            return True
        else:
            return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        #note: will only resize if array is full
        if self.isFull() == True:
            #considering cases when not in order.
            if self.rear == self.front and self.rear != 0:
                #print('the front array is ', self.queue[self.front:])
                #print('the rear array is ', self.queue[:self.rear])
                #rearranges the array so that index 0 is at front of the array
                #then doubles the queue
                self.queue = self.queue[self.front:] + \
                    self.queue[:self.rear] + [None for x in self.queue]


                #reset location of pointers
                self.front = 0
                self.rear = self.numElems

            #this case is for when the array is in order starting from 0
            else:
                #print("the resize function is going here")

                #set location of rear pointer
                self.rear = self.numElems
                self.queue =  self.queue + [None for x in self.queue]
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        #if queue is full, increase size first
        if self.isFull() == True:
            self.resize()

        #insert value
        self.queue[self.rear] = val
        #update counter
        self.numElems = self.numElems + 1
        #update rear pointer, taking into account of being at the end of array
        if self.rear == len(self.queue)-1:
            self.rear = 0
        else:
            self.rear = self.rear + 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        #handles null case
        if self.isEmpty() == True:
            #print(">> Array is empty.")
            return
        else:
            #stores pop value then replaces it with None
            popVal = self.queue[self.front]
            self.queue[self.front] = None

            #update front pointer, taking into account of end of array
            if self.front == len(self.queue)-1:
                self.front = 0
            else:
                self.front = self.front + 1

            #update element
            self.numElems = self.numElems - 1
            return popVal
