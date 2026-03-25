def super_getattribute(super_obj, name):
    cls = super_obj.__thisclass__     # klasa podana w super()
    obj = super_obj.__self__          # instancja
    start_type = type(obj)

    mro = start_type.__mro__

    # find position of cls in MRO
    i = mro.index(cls)

    # search after it
    for base in mro[i+1:]:
        if name in base.__dict__:
            attr = base.__dict__[name]

            if hasattr(attr, "__get__"):
                return attr.__get__(obj, start_type)

            return attr

    raise AttributeError(name)
