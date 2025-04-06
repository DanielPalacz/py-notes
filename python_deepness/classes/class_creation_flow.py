
class CustomMetaclassType(type):
    def __init__(self, name, bases, dct):
        print("[CustomMetaclassType][__init__] Initializing the MyClass object (class level object).")
        print("[CustomMetaclassType][__init__] Class namespace dictionary state -> self.__dict__:", self.__dict__)
        print("[CustomMetaclassType][__init__] Class namespace dictionary state -> dct:", dct) # __classcell__
        super().__init__(name, bases, dct)

    def __new__(cls, name, bases, dct):
        print("[CustomMetaclassType][__new__] Creating a new MyClass object (class level object).")
        print("[CustomMetaclassType][__new__] Class namespace dictionary already exists:", cls.__dict__)
        print("[CustomMetaclassType][__new__] But it will be updated with dictionary coming from prepared hook:", dct)
        return super().__new__(cls, name, bases, dct)


    @classmethod
    def __prepare__(cls, name, bases):
        print("[CustomMetaclassType][__prepare__] Running prepare. Returning {'prepare_list': [1, 2, 3]}")
        return {'prepare_list': [1, 2, 3]}


# print(globals())

class MyClass(metaclass=CustomMetaclassType):
    def __new__(cls, *args, **kwargs):
        print("[MyClass][__new__]Creating a new instance of MyClass.")
        return super().__new__(cls)

    def __init__(self):
        print("[MyClass][__init__]Initializing the instance of MyClass.")

# Create an instance of MyClass
obj = MyClass()
