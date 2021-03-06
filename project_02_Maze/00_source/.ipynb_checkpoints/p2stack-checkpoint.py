"""
Math 560
Project 2
Fall 2020

p2stack.py

Partner 1:
Partner 2:
Date:
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        if self.numElems == len(self.stack):
            #print('Stack is full')
            return True
        else:
            #print('Stack is not full')
            return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            #print('Stack is empty')
            return True
        else:
            #rint('Stack is not empty')
            return False

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        self.stack = self.stack + [None for x in range(len(test.stack))]
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        if self.isFull == False:
            # self.top = self.top + 1
            # self.stack[self.top] = val
            # self.numElems = self.numElems + 1
            print('NOT FULL')
        else:
            print('>>TRUE')
            print('>> Stack is full, resizing...')
            self.resize()
        print('>>after if/else')


        ##### IMPLEMENT! #####
        return

    """
    pop function to pop the value off the top of the stack.
    """
    # def pop(self):
    #     if self.isEmpty == True:
    #         print('>> Stack is empty.')
    #         return
    #
    #     else:
    #
    #     ##### IMPLEMENT! #####
    #     ch = self.stack[self.numElems - 1]
    #     del(self.stack[-1])
    #     self.numElems = self.numElems - 1
    #     return ch


test = Stack()
test.isFull()
test.isEmpty()
len(test.stack)
print(test)
test.push(1)
test.push(1)
test.push(1)

test.numElems
len(test.stack)

test.isFull()
print(test)
test.push(1)
test.resize()
test.push(2)
print(test)


len(test.stack)


print(test)

test.push(99)
print(test)
test.push(55)
print(test)

blue = True

if blue == True:
    print('Blue')
