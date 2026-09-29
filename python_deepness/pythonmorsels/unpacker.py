
class Unpacker:
    def __init__(self, data=None):
        if data is None:
            object.__setattr__(self, '_data', None)
        else:
            object.__setattr__(self, '_data', data.copy())

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getattr__(self, name):
        return self._data[name]

    def __setattr__(self, name, value):
        self._data[name] = value

    def __iter__(self):
        for k, v in self._data.items():
            yield v

    # def __str__(self):
    #     return self.text

    def __repr__(self):
        text = "Unpacker("
        for k, v in self._data.items():
            try:
                v_unpack = int(v)
            except (ValueError, TypeError):
                v_unpack = f"{v!r}"

            text += f'{k}={v_unpack}, '

        text += ')'
        text = text.replace(', )', ')')

        return text
