
class CustomType(type):
    def __init__(self, name, bases, dct):
        print("[__init__] Initializing the MyClass object (class level object).")
        print("[__init__] Class namespace dictionary state:", self.__dict__)
        print("[__init__] Class namespace dictionary state:", dct) # __classcell__
        super().__init__(name, bases, dct)


    def __new__(cls, name, bases, dct):
        print("[__new__] Creating a new MyClass object (class level object).")
        print("[__new__] Class namespace dictionary already exists:", cls.__dict__)
        return super().__new__(cls, name, bases, dct)

# print(globals())

class MyClass(metaclass=CustomType):
    def __new__(cls, *args, **kwargs):
        print("Creating a new instance of MyClass.")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing the instance of MyClass.")

# Create an instance of MyClass
# obj = MyClass()



class A:
    pass


print(dir(A))
