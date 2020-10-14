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
        if self.isFull() == True:
            if self.rear == self.front and self.rear != 0:
                #print('the front array is ', self.queue[self.front:])
                #print('the rear array is ', self.queue[:self.rear])
                self.queue =  self.queue[self.front:] + self.queue[:self.rear] + [None for x in self.queue]
                self.front = 0 #reset location of pointer
                self.rear = self.numElems #reset location of pointer
            else:
                #print("the resize function is going here")
                self.rear = self.numElems
                self.queue =  self.queue + [None for x in self.queue]
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        if self.isFull() == True:
            self.resize()
        self.queue[self.rear] = val
        self.numElems = self.numElems + 1
        if self.rear == len(self.queue)-1: #if at end of array
            self.rear = 0
        else:
            self.rear = self.rear + 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        if self.isEmpty() == True:
            #print("Array is empty.")
            return
        else:
            popVal = self.queue[self.front]
            self.queue[self.front] = None
            if self.front == len(self.queue)-1: #if at end of array
                self.front = 0 #go to the front
            else:
                self.front = self.front + 1
            self.numElems = self.numElems - 1
            return popVal
# def test():
#     test = Queue()
#     print(test)
#     test.push(1)
#     print(test)
#     test.push(2)
#     print(test)
#     test.pop()
#     print(test)
#     test.push(3)
#     print(test)
#
#     test.push(4)
#     print(test)
#     test.resize()
#     print(test)
#
#
#     test.push(5)
#
#     print(test)
#     test.push(6)
#     print(test)
#     test.push(7)
#     print(test)
#     test.push(8)
#     print(test)
#     test.pop()
#     print(test)
#     test.pop()
#     test.pop()
#     test.pop()
#     test.pop()
#     test.pop()
#     test.pop()
#     test.pop()
#     print()
#     test.push(1)
#     print(test)
#     test.pop()
#     print(test)
#     test.push(1)
#     test.push(2)
#     test.push(3)
#     test.push(4)
#     test.push(5)
#     print(test)
#     test.resize()
#     print(test)
#     test.push(6)
#     test.push(7)
#     test.push(8)
#     test.push(9)
#     test.push(10)
#     print(test)
#     test.push(11)
#     test.push(12)
#     print(test)
#     test.push(13)
#     print(test)
#     for x in range(14):
#         test.pop()
#     print(test)

#test()
