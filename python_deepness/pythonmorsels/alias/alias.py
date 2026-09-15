

class alias:
    def __init__(self, target_name, write = False):
        self.target_name = target_name
        self.write = write


    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.target_name)

    def __set__(self, instance, value):
        if self.write:
            setattr(instance, self.target_name, value)
        else:
            raise AttributeError("can't set attribute")



class DataRecord:
    title = alias('serial')

    def __init__(self, serial):
        self.serial = serial


# record = DataRecord("148X")
# record.title = "1ABC"
