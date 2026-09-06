

class EasyDict(dict):

    def __init__(self, *args, normalize=True, **kwargs):
        super().__init__(*args, **kwargs)
        super().__setattr__("normalize", normalize)

    def __getattr__(self, name):
        if "_" in name and self.normalize:
            name = name.replace("_", " ")

        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"Lack of attribute {name}.")

    def __setattr__(self, name, value):
        if "_" in name and self.normalize:
            name = name.replace("_", " ")
        self[name] = value

###

p = EasyDict({'name': "Trey Hunner", 'location': "San Diego", "greeting 1": "Hi"})
