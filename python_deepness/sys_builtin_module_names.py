import sys
print(sys.builtin_module_names)
print(len(sys.builtin_module_names))

B = sys.builtin_module_names

print()
print(sys.modules)
print(len(sys.modules))

FOUND = []
for b in B:
    if b in sys.modules:
        FOUND.append(b)

print(FOUND)
print(len(FOUND))
