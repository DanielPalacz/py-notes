import sys
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def line_tracer():
    def trace(frame, event, arg):
        if event == "line":
            filename = Path(frame.f_code.co_filename)
            lineno = frame.f_lineno
            code_line = open(filename).readlines()[lineno - 1].strip()
            print(f"{filename.name}:{lineno}: {code_line}")
        return trace

    sys.settrace(trace)
    try:
        yield
    finally:
        sys.settrace(None)


def test_func():
    x = 10
    y = 20
    z = x + y
    print("Wynik:", z)

with line_tracer():
    test_func()




# import sys
# from pathlib import Path
# from contextlib import contextmanager
#
# @contextmanager
# def interactive_debugger():
#     def trace(frame, event, arg):
#         if event == "line":
#             filename = Path(frame.f_code.co_filename)
#             lineno = frame.f_lineno
#             code_line = open(filename).readlines()[lineno - 1].strip()
#
#             print(f"\n📍 {filename.name}:{lineno}: {code_line}")
#             print(f"🔍 Lokalne zmienne: {frame.f_locals}")
#
#             while True:
#                 cmd = input("▶ [Enter] = dalej, [q] = zakończ, [v] = pokaż zmienne > ").strip()
#                 if cmd == "":
#                     break
#                 elif cmd == "q":
#                     sys.exit("🛑 Debugowanie przerwane.")
#                 elif cmd == "v":
#                     print(f"🧾 Zmienne: {frame.f_locals}")
#                 else:
#                     print("❓ Nieznane polecenie.")
#
#         return trace
#
#     sys.settrace(trace)
#     try:
#         yield
#     finally:
#         sys.settrace(None)
#
# def test_func():
#     a = 3
#     b = 5
#     c = a * b
#     print("Wynik:", c)
#
# with interactive_debugger():
#     test_func()
