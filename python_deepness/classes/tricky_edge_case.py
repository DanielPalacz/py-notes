
class A:
    from json import dumps as g         # written in Python and defines __get__ (however there can be 2 implementations: Python/C)
    from itertools import repeat as h   # it is callable class written in C, doesn't define __get__

# Notes:
#  * During Runtime when 'class A' is created, class body-content is being executed line by line (like function).
#  * A.g("xx")   - ok
#  * A.h("xx")   - ok
#  * A().g("xx") - TypeError: dumps() takes 1 positional argument but 2 were given
#  * A().h("xx") - ok
#  * @classmethod impact


x1 = A.g("xx")
x2 = A.h("xx")

# x3 = A().g("xx")
# x4 = A().h("xx")
