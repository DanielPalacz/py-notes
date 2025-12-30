import builtins
import dis

from random import randint


original_build_class = builtins.__build_class__


class TypeDebug(type):

    def __init__(cls, what, bases, dct):
        print(f"[TypeDebug][__init__] Calling type.__init__: what={what}, bases={bases}, dct={dct}")
        type.__init__(cls, what, bases, dct)


    def __new__(cls, *args, **kwargs):

        print()

        print(f"[TypeDebug][__new__] Calling type.__new__: args={args}, kwargs={kwargs}")
        print("[TypeDebug][__new__] - locals:", locals())
        print("[TypeDebug][__new__] - locals['__class__']:", dir(locals()["__class__"]))
        return super().__new__(cls, *args, **kwargs)


    def __prepare__(cls, *args, **kwargs):
        print(f"[TypeDebug][__prepare__] Calling type.__prepare__: args={args}, kwargs={kwargs}")
        return {"prepare": 1}


def debug_build_class(*args, **kwargs):
    print(f"[debug_build_class] Calling __build_class__: args={args}, kwargs={kwargs}")
    return original_build_class(*args, **kwargs)


builtins.__build_class__ = debug_build_class


class MagicRandomNumber:

    def __get__(self, obj, objtype=None):
        if self.method == "random.randint":
            return randint(0, 100)
        else:
            raise NotImplemented("Not implemented RandomNumber generation.")

    def __set_name__(self, owner, name):
        print(f" - calling descriptor_obj.__set_name__(self, owner, name)")
        self.method = "random.randint"


print("--------------------------------------------------------------------------------------------------------------------------------------------------------")


class ClassCreationFlowReview(metaclass=TypeDebug):
    print("[ClassCreationFlowReview] Executing code of Class body - start.")
    print("[ClassCreationFlowReview] locals() during Class body execution", locals())
    print("[ClassCreationFlowReview] dir() during Class body execution", dir())

    r = MagicRandomNumber()
    x = 10

    print("[ClassCreationFlowReview] locals() during Class body execution", locals())
    print("[ClassCreationFlowReview] Executing code of Class body - end.")


# Class creation protocol:
#  - builtins.__build_class__
#  - [metaclass].__prepare__
#  - executing code of the given Class body (like function type)
#  - [the given class].__set_name__(cls, descr_name)
#  - [the given class].__new__
#  - [the given class].__init__


# Hooks:
#  - [metaclass].__prepare__
#  - cls.__init_subclass__
#  - cls.__set_name__
