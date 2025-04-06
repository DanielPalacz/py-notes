

class Base:

    def __init_subclass__(cls, **kwargs):
        assert hasattr(cls, "boo"), "Lack of boo attribute declaration. Derived classes expect to have it, failing."

    def foo(self):
        return "foo"



class Derived(Base):
    def bar(self):
        return self.boo()



# def _():
#     class Base:
#         pass
#
# from dis import dis
# dis(_)
