
class ReadOnlyVar:
    def __set_name__(self, _, name):
        # _ is owner class object
        self.__attr_name = name

    def __init__(self, value):
        self.__value = value

    def __get__(self, obj, objtype=None):
        return self.__value

    def __set__(self, obj, value):
        raise AttributeError(f"Attribute '{self.__attr_name} is read-only and can't be override.'")

# then
#
# class A:
#     var_ro = ReadOnlyVar("Constant data.")
#
# then
#
# object_x = A()
# object_x.var_reado = "New value"  # not possible