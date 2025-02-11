
def value():
    _item = None

    def read():
        return _item

    def update(item):
        nonlocal _item
        _item= item

    def closure():
        pass

    closure.read = read
    closure.update = update
    return closure


v = value()

