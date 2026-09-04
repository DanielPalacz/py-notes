
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
