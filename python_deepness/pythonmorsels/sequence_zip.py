
class SequenceZip:

    def __init__(self, *args):
        self.zip_args = list(args)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return SequenceZip(
                *(seq[:len(self)][index] for seq in self.zip_args)
            )

        if index < 0:
            index += len(self)

        if index < 0 or index >= len(self):
            raise IndexError

        return tuple(seq[index] for seq in self.zip_args)

    def __iter__(self):
        for i in range(len(self)):
            yield tuple(seq[i] for seq in self.zip_args)

    def __len__(self):
        try:
            return min(len(za) for za in self.zip_args)
        except ValueError:
            return 0

    def __str__(self):
        return f"SequenceZip({', '.join(repr(arg) for arg in self.zip_args)})"

    def __repr__(self):
        return f"SequenceZip({', '.join(repr(arg) for arg in self.zip_args)})"

    def __eq__(self, other):
        if not isinstance(other, SequenceZip):
            return NotImplemented
        return list(self) == list(other)

