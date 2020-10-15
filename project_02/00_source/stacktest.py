from p2stack import *


if __name__ == "__main__":
	test_stack = Stack()
	for i in range(10):
		test_stack.push(i)
		print(test_stack)
	for i in range(10):
		test_stack.pop()
		print(test_stack)
	for i in range(10):
		test_stack.push(i)
		print(test_stack)