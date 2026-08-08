import heapq


# heapify() - Zamienia zwykłą listę w kopiec.

numbers = [5, 2, 8, 1, 9]

heapq.heapify(numbers)

print(numbers)



# heappush() - Dodaje element.

# heap = []
#
# heapq.heappush(heap, 5)
# heapq.heappush(heap, 2)
# heapq.heappush(heap, 8)
# heapq.heappush(heap, 1)
#
# print(heap)
#
# [1, 2, 8, 5]
#
# Koszt:
#
# O(log n)
