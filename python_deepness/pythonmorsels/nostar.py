
class Something:

    def __getitem__(self, index):
        raise ImportError("No star imports!")

    def __iter__(self):
        raise ImportError("No star imports!")


__all__ = Something()


tau = 6.283185307179586
