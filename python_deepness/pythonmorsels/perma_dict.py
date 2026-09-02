

class PermaDict(dict):

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"{key!r} is already in dictionary.")

        super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            self[key] = value

d = PermaDict()
d.update({"a": 1})

