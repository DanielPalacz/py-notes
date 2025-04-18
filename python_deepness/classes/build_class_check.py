import builtins
import dis

from random import randint

original_build_class = builtins.__build_class__

class TypeDebug(type):

    def __init__(cls, what, bases, dct):
        # print(f"Wywołanie type.__init__: what={what}, bases={bases}, dct={dct}")
        print(f"Calling type.__init__: what={what}, bases={bases}, dct={dct}")
        type.__init__(cls, what, bases, dct)


    def __new__(cls, *args, **kwargs):
        print(f"Calling type.__new__: args={args}, kwargs={kwargs}")
        print(" - locals:", locals())
        print(" - locals['__class__']:", dir(locals()["__class__"]))
        return super().__new__(cls, *args, **kwargs)


    def __prepare__(cls, *args, **kwargs):
        print(f"Calling type.__prepare__: args={args}, kwargs={kwargs}")
        return {"prepare": 1}


def debug_build_class(*args, **kwargs):
    print(f"Calling __build_class__: args={args}, kwargs={kwargs}")
    return original_build_class(*args, **kwargs)


builtins.__build_class__ = debug_build_class


class MagicRandomNumber:

    def __get__(self, obj, objtype=None):
        if self.method == "random.randint":
            return randint(0, 100)
        else:
            raise NotImplemented("Not implemented RandomNumber generation.")

    def __set_name__(self, owner, name):
        print(f" # Calling descriptor_obj.__set_name__(self, owner, name)")
        self.method = "random.randint"



class ClassCreationFlowReview(metaclass=TypeDebug):
    print()
    print("Executing code of Class body - start.")
    print(" * locals() during Class body execution", locals())
    print("   - dir() during Class body execution", dir())


    r = MagicRandomNumber()
    x = 10

    # @staticmethod
    # def method():
    #     return super()  # Using super() triggers adding __classcell__ to Namespace

    print(" * locals() during Class body execution", locals())
    print(" * Executing code of Class body - end.")
    print()
    # super().__dict__




print()
# print(ClassCreationFlowReview().prepare)
print("Magic number is:", ClassCreationFlowReview().r)

# class B(A):
#     y = 20

# C = type("C", (object,), {"z": 30})
# print(dir())
# __builtins__.__build_class__("C", (object,), {"z": 30})



# Class creation protocol:
# 1. builtins.__build_class__(*(A, "A"), **{'metaclass': <class '__main__.TypeDebug'>})
#    - A is function type

# Here: [metaclass].__prepare__ is triggered

# 2. Executing code of Class body (like function type)
#    - triggering cls.__set_name__(cls, descr_name)

# 3. type.__new__(class_name, (BaseClass1, ...), {'__module__': '__main__', '__qualname__': class_name, 'class_attr': class_attr_value})
#    - it creates instance of class object that will be used by __init__ method

# 4. type.__init__(cls, class_name, (BaseClass1, ...), {'__module__': '__main__', '__qualname__': class_name, 'class_attr': class_attr_value})
#    - triggering hook: 'cls.__init_subclass__'

# Hooks:
#  - [metaclass].__prepare__
#  - cls.__init_subclass__
#  - cls.__set_name__
