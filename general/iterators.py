class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.current < self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration  # No more items to iterate over

# Using the custom iterator
square_iter2 = SquareIterator(3)  # Squares from 0^2 to 3^2 and raises StopIteration
print(next(square_iter2))
print(next(square_iter2))
print(next(square_iter2))
print(next(square_iter2))
