
SENTINEL = object()


class DontWantSelf:
    def __init__(dont_want_self, a):
        dont_want_self.a = a
        print("[__init__ call] Checking if 'dont_want_self' can be used instead of 'self':", dont_want_self)

    print("[DontWantSelf Class creation time] - checking '__init__' function object type:", type(__init__))

    def __getattr__(dont_want_self, value):
        return SENTINEL

    def check_instance_method(dont_want_self):
        print("[check_instance_method call] Checking if 'dont_want_self' can be used instead of 'self':", dont_want_self)
        print("[check_instance_method call] Checking function type:", dont_want_self.check_instance_method)


    print("[DontWantSelf Class creation time] - checking 'check_instance_method' function object type:", type(check_instance_method))


# d_obj = DontWantSelf("a_arg")
# d_obj.check_instance_method()
# print(d_obj.a)
#
#
# print(DontWantSelf("A1").a)
# print(DontWantSelf("A1").b)
# print(DontWantSelf("A1").c)
# print()
#
#
# print(type(DontWantSelf("A1").check_instance_method))
# print(type(DontWantSelf.check_instance_method))


class NoClsArg:

    @classmethod
    def check_class_method(dont_want_cls):
        print("[check_class_method call] Checking if 'dont_want_self' can be used instead of 'self':", dont_want_cls)
        print("[check_class_method call] Checking function type:", dont_want_cls.check_class_method)

    print("[NoClsArg Class creation time] - checking 'check_class_method' function object type:", type(check_class_method))


    @staticmethod
    def check_static_method():
        print("[check_class_method call] Checking function type:", NoClsArg.check_static_method)

    print("[NoClsArg Class creation time] - checking 'check_static_method' function object type:", type(check_static_method))

    def func():
        print("[func call] Checking function type:", NoClsArg.func)

    print("[NoClsArg Class creation time] - checking 'func' function object type:", type(func))


no_cls_obj = NoClsArg()
print(no_cls_obj.check_static_method)
print(no_cls_obj.func)
