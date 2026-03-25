def object_getattribute(obj, name):
    cls = type(obj)

    # 1. data descriptor
    if name in cls.__dict__:
        attr = cls.__dict__[name]
        if hasattr(attr, "__set__"):
            return attr.__get__(obj, cls)

    # 2. instance dict
    if name in obj.__dict__:
        return obj.__dict__[name]

    # 3. non-data descriptor or class attr
    if name in cls.__dict__:
        attr = cls.__dict__[name]
        if hasattr(attr, "__get__"):
            return attr.__get__(obj, cls)
        return attr

    # 4. MRO search (pominięte tu dla prostoty)

    raise AttributeError
