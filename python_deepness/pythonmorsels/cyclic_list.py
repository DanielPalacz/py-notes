

# Base Problem, Bonus 1 + Bonus 2

class CyclicList(list):

    def __iter__(self):
        length = len(self)
        tmp = 0

        while True:
            yield self[tmp]
            tmp += 1
            if tmp == length:
                tmp = 0


    def __getitem__(self, index):
        length = len(self)
        if index >= length:
            index -= length

        return super().__getitem__(index)


    def __setitem__(self, index, value):
        length = len(self)
        if index >= length:
            index -= length

        super().__setitem__(index, value)










































# Bonus 3

# class CyclicList(list):
#
#     def __iter__(self):
#         length = len(self)
#         tmp = 0
#
#         while True:
#             yield self[tmp]
#             tmp += 1
#             if tmp == length:
#                 tmp = 0
#
#     def __getitem__(self, index):
#         length = len(self)
#
#         if isinstance(index, slice):
#             start = index.start
#             stop = index.stop
#             step = index.step or 1
#
#             if start is None:
#                 start = 0 if step > 0 else length - 1
#
#             if stop is None:
#                 stop = length if step > 0 else -1
#
#                 # For slices such as [-3:], preserve normal slice behavior.
#                 if start < 0:
#                     start %= length
#
#             return [
#                 super().__getitem__(i % length)
#                 for i in range(start, stop, step)
#             ]
#
#         return super().__getitem__(index % length)
#
#     def __setitem__(self, index, value):
#         length = len(self)
#
#         if isinstance(index, slice):
#             raise TypeError("Cyclic slicing assignment is not supported")
#
#         super().__setitem__(index % length, value)
