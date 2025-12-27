
# What is the design thinking behind `@classmethod`?
#
# Primary design pressure:
# - High fan-out at object construction boundaries
#
# Premises:
# - Object creation is a high-impact API surface:
#   constructor signatures tend to be referenced widely and are costly to change.
# - Churn arises from unstable or heterogeneous construction semantics, such as:
#   - multiple input formats (files, JSON, env, network)
#   - differing validation or normalization paths
#   - evolving invariants
# - Overloading `__init__` to handle all modalities concentrates instability in a
#   single, high–fan-out method.
#
# Key considerations:
# - We want to preserve a single internal initialization contract.
# - We want construction logic to evolve without forcing downstream rewrites.
# - We want subclass-friendly construction that returns the appropriate concrete type.
#
# Conclusion:
# - We need a way to decompose object creation into multiple, named, evolvable
#   construction pathways while keeping them logically attached to the class.
# - `@classmethod` provides this by:
#   - binding constructors to the class rather than the instance,
#   - enabling alternative constructors (`from_*`, `load_*`, etc.),
#   - and centralizing invariants without inflating `__init__`.


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