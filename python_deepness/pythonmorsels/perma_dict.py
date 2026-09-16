
class PermaDict(dict):

    def __init__(self, *args, silent: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.silent = silent

    def __setitem__(self, key, value):
        if key in self:
            if self.silent:
                return None
            else:
                raise KeyError(f"{key!r} is already in dictionary.")

        super().__setitem__(key, value)
        return None

    def update(self, *args, force: bool = False, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            if force:
                super().__setitem__(key, value)
            else:
                self[key] = value

    def force_set(self, key, value):
        super().__setitem__(key, value)


# d = PermaDict()
# d.update({"a": 1})
#