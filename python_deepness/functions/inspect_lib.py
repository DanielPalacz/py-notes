
import inspect

def funkcja(a, b: int, c=10, *args, d, e=5, **kwargs):
    pass

sig = inspect.signature(funkcja)

print(sig)


for name, param in sig.parameters.items():
    print(f"Nazwa: {name}")
    print(f"  kind: {param.kind}")
    print(f"  default: {param.default}")
    print(f"  annotation: {param.annotation}")
