def type_getattribute(cls, name):
    # 1. search in metaclass (rare, but real)
    meta = type(cls)
    if name in meta.__dict__:
        attr = meta.__dict__[name]
        if hasattr(attr, "__get__"):
            return attr.__get__(cls, meta)
        return attr

    # 2. search in class MRO
    for base in cls.__mro__:
        if name in base.__dict__:
            attr = base.__dict__[name]

            # descriptors still apply
            if hasattr(attr, "__get__"):
                return attr.__get__(None, cls)

            return attr

    raise AttributeError(name)
