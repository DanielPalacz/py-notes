
class CustomSeq:
    def __getitem__(self, index):
        if index >= 5:
            raise IndexError
        return index * 2

obj = CustomSeq()
iter_custom_seq = iter(obj)
numbers = [elem for elem in iter_custom_seq] # # [0, 2, 4, 6, 8]
# print(obj[2])  # 4 - It works due to __getitem__
# print(list(obj))  # [0, 2, 4, 6, 8] (Python uses __getitem__ to simulate iteration)
