from p2queue import *


if __name__ == "__main__":
	test_queue = Queue()
	for i in range(3):
		print(i)
		test_queue.push(i)
		print(test_queue)
	for i in range(2):
		print(i)
		test_queue.pop()
		print(test_queue)
	for i in range(5):
		print(i)
		test_queue.push(i)
		print(test_queue)