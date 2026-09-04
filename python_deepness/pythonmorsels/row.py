

class Row:

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            super().__setattr__(k, v)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"Lack of attribute {name}.")

    def __setattr__(self, name, value):
        self[name] = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        class_name = self.__class__.__name__

        str_representation = f"{class_name}("

        for k, v in self.__dict__.items():
            str_representation += f"{k}={v!r}, "
        else:
            str_representation += ")"
            str_representation = str_representation.replace(', )', ')')

        return str_representation



class UniqueRow(Row):
    pass
