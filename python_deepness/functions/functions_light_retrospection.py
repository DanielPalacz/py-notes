import dis
import inspect
import sys
import io

def funct():
    pass


def f(a, b=5):
    return a + b

f_source = inspect.getsource(f)
# f_disasembled_bytecode = dis.dis(f)

print(f_source)
# print(f_disasembled_bytecode)

# Tworzymy obiekt StringIO do przechwycenia outputu
output = io.StringIO()
# Przekierowanie standardowego wyjścia
sys.stdout = output
dis.dis(f)
sys.stdout = sys.__stdout__  # Przywracamy normalne wyjście

# Zapisujemy wynik do zmiennej
f_disasembled_bytecode = output.getvalue()
print(f_disasembled_bytecode)

#
print(type(f))
print(dir(f))
# <class 'function'>
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__',
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__',
# '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__']

print(type(f.__code__)) # PyCodeObject
print(dir(f.__code__)) # PyCodeObject
# <class 'code'>
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code',
# 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lines',
# 'co_linetable', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_posonlyargcount', 'co_stacksize', 'co_varnames',
# 'replace']