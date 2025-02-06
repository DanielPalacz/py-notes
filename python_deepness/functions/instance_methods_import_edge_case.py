

def funct(self):
    pass

class A:
    f = funct
    funct2 = list.append

    from json import dumps as g         # it is written in Python so it defines __get__ as all functions written in Python are descriptors
                                        #   - the interesting is there are 2 json implementations Python and C
                                        #   - it is about json mechanics details, not high level functions like dumps

    from itertools import repeat as h   # it is written in C and it doesn't define __get__
                                        #   - also repeat is class object


a = A()
print(a.f)
print(a.g)
print(a.h)

A.g("ggg")
# print(a.g("gggg"))
for obj in a.h("repeating"):
   print(obj)
   break
