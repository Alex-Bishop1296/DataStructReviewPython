from collections import deque

# Implementing a normal queue in python
list_queue = []

# Adding elements to a queue
list_queue.append('a')
list_queue.append('b')
list_queue.append('c')

print("Printing queue", list_queue)

# Removing elements from the queue
print("Elements removed from queue")
# Remove the elements from the front due to FIFO structure 
print(list_queue.pop(0))
print(list_queue.pop(0))
print(list_queue.pop(0))

print("Elements after ", list_queue)

# Initializing a queue with collections deque, has O(1) advantage for dequeue and enqueue operations over list's O(1)
col_deque = deque()
 
# Adding elements to a queue
col_deque.append('a')
col_deque.append('b')
col_deque.append('c')
 
print("Initial queue")
print(col_deque)
 
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(col_deque.popleft())
print(col_deque.popleft())
print(col_deque.popleft())
 
print("\nQueue after removing elements")
print(col_deque)


# Python program to
# demonstrate implementation of
# queue using queue module
 
 
from queue import Queue
 
# Initializing a queue
q = Queue(maxsize = 3)
 
# qsize() give the maxsize
# of the Queue
print(q.qsize())
 
# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')
 
# Return Boolean for Full
# Queue
print("\nFull: ", q.full())
 
# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
 
# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())
 
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
 
# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())