
# What is the design thinking behind `@classmethod`?
#  - FAN-OUT changes are problematic

    # Premises:
    #  - "churn" is often a consequence of interacting with the outside world


# Conclusion:
#  - "We may want to (nominally) decompose bounded modalities associated with data loading."
#  - example with classmethod and multiple constructors

from json import load as json_load

class A:

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_plain(cls, filename):
        with open(filename) as f:
            data = f.read()
        return cls(data)

    @classmethod
    def from_json(cls, fillename, *, json_key=None):
        with open(fillename) as f:
            data = json_load(f)
            if json_key is not None:
                data = data[json_key]
        return cls(data)

    @classmethod
    def from_pickle(cls, filename):
        ...

    @classmethod
    def from_xml(cls, filename):
        ...