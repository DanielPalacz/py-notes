from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.appendleft(5)

print(dq)          # deque([5, 10, 20])

dq.pop()
print(dq)          # deque([5, 10])

dq.popleft()
print(dq)          # deque([10])


# Why use deque instead of a list?
#
# Removing the first element from a list is slow because all remaining elements must be shifted:
#
# lst.pop(0)    # O(n)
#
# With a deque:
#
# dq.popleft()  # O(1)
#
# This makes deque ideal for:
#
# Implementing queues (FIFO)
# Implementing stacks (LIFO)
# Breadth-First Search (BFS) in graphs and trees
# Sliding window algorithms
