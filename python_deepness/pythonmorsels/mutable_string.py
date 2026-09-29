
class MutableString:

    def __init__(self, text: str = ""):
        self.text = list(str(text))

    def __add__(self, other):
        return "".join(self.text) + str(other)

    def __call__(self):
        return "".join(self.text)

    def __contains__(self, item):
        return str(item) in "".join(self.text)

    def __str__(self):
        return f'{"".join(self.text)}'

    def __repr__(self):
        return f"{"".join(self.text)!r}"

    def __eq__(self, other):
        return "".join(self.text) == other

    def __len__(self):
        return len("".join(self.text))

    def __getitem__(self, index):
        result = self.text[index]

        if isinstance(index, slice):
            return MutableString("".join(result))

        return result

    def __setitem__(self, key, value):
        self.text[key] = value

    def endswith(self, part):
        return "".join(self.text).endswith(part)

    def lower(self):
        return "".join(self.text).lower()

    def replace(self, x, y):
        return "".join(self.text).replace(x, y)

    def upper(self):
        return "".join(self.text).upper()
