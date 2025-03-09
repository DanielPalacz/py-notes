

def funct(self):
    pass

class A:
    f = funct
    funct2 = list.append

    from json import dumps as g         # it is written in Python so it defines __get__ as all functions Python written are descriptors
                                        #   - the interesting is there are 2 json implementations Python and C
                                        #   - it is about json mechanics details, not high level functions like dumps

    from itertools import repeat as h   # it is written in C, so it doesn't define __get__
                                        #   - also repeat is class object

    gx = classmethod(g)
    hx = classmethod(h)

a = A()

print(dir(A.g))
print(a.f)
print(a.g)
print(a.h)

print(A.g)
print(A.g("sss"))
# print(a.g("sss")) # created new bound method so call passes 2 args: self, 'sss' -> it causes error
print(A.g("sss"))
# print(A.gx("sss")) # TypeError: dumps() takes 1 positional argument but 2 were given


print(A.h("zzz"))
print(a.h("sss"))
print(A.hx)

print(A.hx(123))
# Here is called repeat constructor only. It works, but it's not the intended or correct behavior.
# the fact that hx works is more of a quirk of how Python handles callable classes than the intended use of classmethod
