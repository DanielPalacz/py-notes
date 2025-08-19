# #
# #
# #
# # def call(args, kwargs):
# #     print("fake call print")
# #     args[0](*args[1:], **kwargs)
# #
# #
# #
# def print_x1():
#     print("x1")
# #
# # print_x1.__call__ = call
# #
# #
# #
# #
# # import ctypes
# #
# # # Raw bytes, header + data + what left
# # s1_addreess = id(print_x1.__class__.__name__)
# # # raw_bytes = ctypes.string_at(s1_addreess, 2)
# #
# # # text = []
# # # for num in range(1000):
# # #     _raw_byte = ctypes.string_at(s1_addreess + num, 1)
# # #
# # #     try:
# # #         str_byte = _raw_byte.decode("utf-8").__str__()
# # #         if 1 < ord(str_byte) < 130:
# # #             text.append(str_byte)
# # #     except UnicodeDecodeError:
# # #         print("UnicodeDecodeError")
# #
# #
# #
# # # for i in range(3000):
# # #     # print(i, "-", f"\traw_bytes[{i}]:", raw_bytes[i])
# # #     # print("  - ", chr(raw_bytes[i]))
# # #
# # #     if  chr(raw_bytes[i]) == "f":
# # #         print("offset", i)
# # #
# # #     if raw_bytes[i] == bytes("f", "utf-8"):
# # #         print("offset_b", i)
# # #
# # #     # if bytes("f", "utf-8") in raw_bytes:
# # #     #     breakpoint()
# #
# #
# #
# #
# # # raw_bytes_copy = (ctypes.c_char * len(raw_bytes)).from_buffer_copy(raw_bytes)
# # # print(S1)
# # # print(S1)
# #
# # # raw_bytes_copy[48] = b'*'[0]
# # # raw_bytes_copy[49] = b'F'[0]
# # # raw_bytes_copy[50] = b'u'[0]
# # # raw_bytes_copy[51] = b'n'[0]
# # # raw_bytes_copy[52] = b't'[0]
# # # raw_bytes_copy[53] = b'i'[0]
# # # raw_bytes_copy[54] = b'o'[0]
# # # raw_bytes_copy[55] = b'n'[0]
# # # print(S1)
# #
# #
# # #
# # # # The PyUnicodeObject struct is complex; instead, get UTF-8 encoded bytes pointer:
# # # # Luckily, CPython provides a C API to get utf8 pointer, but no direct way here.
# # # # So fallback to:
# # # utf8_bytes = s.encode('utf-8')
# # #
# # # print(utf8_bytes)  # b'function'
# # #
# # # for i, b in enumerate(utf8_bytes):
# # #     print(i, "-", chr(b))
# # #
# #
# import ctypes
#
# ADDRESS_GLOBAL = None
# RAW_CHARS = None
#
#
# class PyASCIIObject(ctypes.Structure):
#     _fields_ = [
#         ("ob_refcnt", ctypes.c_ssize_t),
#         ("ob_type", ctypes.c_void_p),
#         ("length", ctypes.c_ssize_t),
#         ("hash", ctypes.c_ssize_t),
#         ("state", ctypes.c_uint),
#         ("wstr", ctypes.c_void_p),
#     ]
#
# def read_raw_bytes(obj):
#     addr = id(obj)
#     ascii_obj = PyASCIIObject.from_address(addr)
#     length = ascii_obj.length
#     state = ascii_obj.state
#
#     compact = (state >> 6) & 1
#     ascii_flag = (state >> 0) & 1
#     kind = (state >> 2) & 7
#
#     print(locals())
#
#
#
# #
# #     if compact and ascii_flag:
# #         # Compact ASCII - 1 bajt na znak
# #         data_addr = addr + ctypes.sizeof(PyASCIIObject)
# #         raw_chars = (ctypes.c_char * length).from_address(data_addr)
# #         return bytes(raw_chars)
# #     else:
# #         # W innych wypadkach może być 2 lub 4 bajty
# #         # przykład: 2 bajty na znak
# #         global ADDRESS_GLOBAL
# #         ADDRESS_GLOBAL = addr + ctypes.sizeof(PyASCIIObject)
# #
# #
# #         if kind == 1:
# #             global RAW_CHARS
# #             RAW_CHARS = (ctypes.c_uint16 * length).from_address(ADDRESS_GLOBAL)
# #
# #             return bytes(RAW_CHARS)
# #
# #         elif kind == 2:
# #             raw_chars = (ctypes.c_uint32 * length).from_address(ADDRESS_GLOBAL)
# #             return bytes(raw_chars)
# #         else:
# #             # fallback
# #             return print_x1.__class__.__name__.encode('utf-8')
# #
#
# read_raw_bytes("function")
# read_raw_bytes(print_x1.__class__.__name__)
#
# # # raw = read_raw_bytes(print_x1.__class__.__name__)
# # # chars = list(RAW_CHARS)
# # # chars_raw = list(raw)
# # # print(chars)
# # # print(chars_raw)
# # # # print([31056, 21087, 28773, 114, 27136, 25445, 116, 101])
# # # # s = ''.join(chr(c) for c in chars)
# # #
# # # # import struct
# # # # bytes_raw = b''.join(struct.pack('<H', c) for c in RAW_CHARS)
# # # # print(bytes_raw)  # surowe dane UTF-16LE
# #
# # # import ctypes
# # # import struct
# # #
# # # # Obiekt do zbadania
# # # s = print_x1.__class__.__name__  # "function"
# # #
# # # # Adres bazowy
# # # addr = id(s)
# # #
# # # # Odczyt pól z nagłówka (zakładamy CPython i 64-bit)
# # # # Pomijamy PyObject_HEAD (16 bajtów) i wczytujemy:
# # # length = ctypes.c_uint.from_address(addr + 16).value
# # # state  = ctypes.c_uint.from_address(addr + 24).value
# # #
# # # kind = (state >> 0) & 7
# # # compact = (state >> 6) & 1
# # # ascii_flag = (state >> 7) & 1
# # #
# # # print(f"length={length}, kind={kind}, compact={compact}, ascii_flag={ascii_flag}")
# # # import ctypes
# # #
# # # class PyASCIIObject(ctypes.Structure):
# # #     _fields_ = [
# # #         ("ob_refcnt", ctypes.c_ssize_t),
# # #         ("ob_type", ctypes.c_void_p),
# # #         ("length", ctypes.c_ssize_t),
# # #         ("hash", ctypes.c_ssize_t),
# # #         ("state", ctypes.c_uint),
# # #         ("wstr", ctypes.c_void_p)
# # #     ]
# # #
# # # addr = id(print_x1.__class__.__name__)
# # # ascii_obj = PyASCIIObject.from_address(addr)
# # #
# # # length = ascii_obj.length
# # # state = ascii_obj.state
# # # kind = (state >> 0) & 7
# # # compact = (state >> 6) & 1
# # # ascii_flag = (state >> 7) & 1
# # #
# # # print(f"length={length}, kind={kind}, compact={compact}, ascii_flag={ascii_flag}")
# # # s = print_x1.__class__.__name__
# #
# #
# # # print(s)
# # # print(repr(s))
# # # print(list(map(ord, s)))
# # # offset = ctypes.sizeof(PyASCIIObject)
# # # raw_bytes = ctypes.string_at(addr, offset + length)
# # # print(raw_bytes)
# # #
# # #
# # # raw_bytes_copy = (ctypes.c_char * len(raw_bytes)).from_buffer_copy(raw_bytes)
# # # print(1, offset, s)
# # # raw_bytes_copy[48] = b'*'[0]
# # # print(2, offset, s)
# # # print(3, offset, print_x1.__class__.__name__)
# # #
# # #
# # #
# # # addr2 = id(print_x1.__class__.__name__)
# # # addr3 = id(raw_bytes)
# # #
# # #
# # #
# # # ctypes.memmove(addr3, raw_bytes_copy, len(raw_bytes_copy))
# # # print(4, offset, print_x1.__class__.__name__)
# # #
# # #
# # # print()
# # # print(raw_bytes)
# # # print(raw_bytes_copy)
# # # print(print_x1.__class__.__name__)
# # #
# # # import ctypes
# # #
# # # def print_x1(): pass
# # # name_obj = print_x1.__class__.__name__
# # #
# # # print("Before:", name_obj)  # 'function'
# # #
# # # # 🧠 Adres danych stringa
# # # addr = id(name_obj)
# # #
# # # class PyASCIIObject(ctypes.Structure):
# # #     _fields_ = [
# # #         ('ob_refcnt', ctypes.c_ssize_t),
# # #         ('ob_type', ctypes.c_void_p),
# # #         ('length', ctypes.c_ssize_t),
# # #         ('hash', ctypes.c_ssize_t),
# # #         ('state', ctypes.c_uint),
# # #         ('wstr', ctypes.c_void_p),
# # #     ]
# # #
# # # pyascii = PyASCIIObject.from_address(addr)
# # #
# # # length = pyascii.length
# # # state = pyascii.state
# # # kind = state & 0b111
# # # compact = (state >> 5) & 1
# # # ascii_flag = (state >> 6) & 1
# # #
# # # assert compact == 1, "Not a compact string"
# # # assert kind == 0, f"Expected ascii (kind=0), but is: {kind}"
# # # assert ascii_flag == 1, "Expected ascii_flag=1"
# # #
#
# # # # 🧮 Offset po strukturze do danych
# # # offset = ctypes.sizeof(PyASCIIObject)
# # # data_addr = addr + offset
# # #
# # # # 🧬 Wartość do nadpisania
# # # new_val = b"hackedfn"  # 8 bajtów
# # # assert len(new_val) == length
# # #
# # # # ✏️ Nadpisanie w pamięci
# # # ctypes.memmove(data_addr, new_val, len(new_val))
# # #
# # # # ✅ Sprawdź efekt
# # # print("After :", print_x1.__class__.__name__)
# #
# #
# #
# #
# # import ctypes
# #
# # def print_x1(): pass
# # name_obj = print_x1.__class__.__name__
# #
# # print("Before:", name_obj)
# #
# # addr = id(name_obj)
# #
# # class PyASCIIObject(ctypes.Structure):
# #     _fields_ = [
# #         ('ob_refcnt', ctypes.c_ssize_t),
# #         ('ob_type', ctypes.c_void_p),
# #         ('length', ctypes.c_ssize_t),
# #         ('hash', ctypes.c_ssize_t),
# #         ('state', ctypes.c_uint),
# #         ('wstr', ctypes.c_void_p),
# #     ]
# #
# # pyascii = PyASCIIObject.from_address(addr)
# #
# # length = pyascii.length
# # state = pyascii.state
# # kind = state & 0b111
# # compact = (state >> 5) & 1
# #
# # assert compact == 1
# # assert kind == 4  # ✅ teraz dopuszczamy 4-bajtowe znaki
# #
# # # offset do danych
# # offset = ctypes.sizeof(PyASCIIObject)
# # data_addr = addr + offset
# #
# # # Nowa wartość (maks. 8 znaków, każdy 4 bajty)
# # new_text = "hackedfn"
# # assert len(new_text) == length
# #
# # # Zamiana tekstu na bajty UCS-4 (little-endian 4 bajty na znak)
# # new_bytes = b''.join((ord(c)).to_bytes(4, 'little') for c in new_text)
# #
# # # Nadpisanie danych
# # ctypes.memmove(data_addr, new_bytes, len(new_bytes))
# #
# # # Test
# # print("After :", print_x1.__class__.__name__)
#
# import sys
#
# s1 = "function"
# s2 = sys.intern("function")
#
# print(s1 is s2)  # najczęściej True
#
# s1 = "function"
# s2 = sys.intern("function")
#
# print(s1 is s2)  # najczęściej True
#
# s1 = "function"
# s2 = str("function")  # wymusza nowy obiekt
#
# # s1 == s2
#
# # print(id(sys.intern(s2)))     # równe id(s1), jeśli s1 był internowany
#
# import ctypes
#
# class PyASCIIObject(ctypes.Structure):
#     _fields_ = [
#         ("ob_refcnt", ctypes.c_ssize_t),
#         ("ob_type", ctypes.c_void_p),
#         ("length", ctypes.c_ssize_t),
#         ("hash", ctypes.c_ssize_t),
#         ("state", ctypes.c_uint),
#         ("wstr", ctypes.c_void_p),
#     ]
#
# # def parse_state(state):
# #     return {
# #         'ascii':         (state >> 0) & 1,
# #         'ready':         (state >> 1) & 1,
# #         'kind':          (state >> 2) & 0b111,
# #         'compact':       (state >> 5) & 1,
# #         'ascii_compact': (state >> 6) & 1,
# #         'interned':      (state >> 7) & 0b11,
# #     }
#
# def inspect_string_state(py_str):
#     if not isinstance(py_str, str):
#         raise TypeError("Only string objects supported.")
#
#     addr = id(py_str)
#     ascii_obj = PyASCIIObject.from_address(addr)
#     state_raw = ascii_obj.state
#     decoded = parse_state(state_raw)
#
#     print(f"[INFO] String: {py_str!r}")
#     print(f"       id: 0x{addr:x}")
#     print(f"       length: {ascii_obj.length}")
#     print(f"       state: {state_raw}  (0b{state_raw:032b})")
#     print("       Decoded flags:")
#     for k, v in decoded.items():
#         print(f"         {k}: {v}")
#
#     return decoded
#
#
# inspect_string_state("function")
# inspect_string_state(print.__class__.__name__)
# inspect_string_state(print_x1.__class__.__name__)
#
#
#
# # class PyCompactUnicodeObject(ctypes.Structure):
# #     _fields_ = [
# #         ("ob_refcnt", ctypes.c_ssize_t),
# #         ("ob_type", ctypes.c_void_p),
# #         ("length", ctypes.c_ssize_t),
# #         ("hash", ctypes.c_ssize_t),
# #         ("state", ctypes.c_uint),
# #         ("wstr", ctypes.c_void_p),
# #         ("utf8", ctypes.c_char_p),        # <--- dodatkowe
# #         ("utf8_length", ctypes.c_ssize_t) # <--- dodatkowe
# #     ]
# #
# # s = print_x1.__class__.__name__
# # addr = id(s)
# # _ = s.encode("utf-8")  # wymusi zbudowanie pola `utf8`
# #
# # u = PyCompactUnicodeObject.from_address(addr)
#
#
# # print(f"[INFO] Extracted UTF-8 ptr: {u.utf8}")
# # print(f"[INFO] Extracted UTF-8 len: {u.utf8_length}")
# # print(f"[INFO] Decoded: {ctypes.string_at(u.utf8, u.utf8_length).decode('utf-8')}")
#
#
# def debug_string_flags(obj):
#     addr = id(obj)
#     ascii_obj = PyASCIIObject.from_address(addr)
#     state = ascii_obj.state
#     kind = (state >> 2) & 0b111
#     compact = (state >> 6) & 1
#     ascii_flag = (state >> 0) & 1
#     interned = (state >> 28) & 0b11
#     print(f"[INFO] kind={kind}, compact={compact}, ascii={ascii_flag}, interned={interned}")
#     return kind, compact, ascii_flag
#
#
# s = print_x1.__class__.__name__
# _ = s.encode("utf-8")
#
# # kind, compact, ascii_flag =  debug_string_flags(s)
# #
# # if compact:
# #     u = PyCompactUnicodeObject.from_address(id(s))
# #     print(f"utf8 ptr: {u.utf8}")
# #     if u.utf8:
# #         raw = ctypes.string_at(u.utf8, u.utf8_length)
# #         print(f"[UTF-8] {raw}")
# #         print(f"[Decoded] {raw.decode('utf-8')}")
# #     else:
# #         print("[WARN] utf8 is NULL")
#
#
# import ctypes
#
# class PyASCIIObject(ctypes.Structure):
#     _fields_ = [
#         ("ob_refcnt", ctypes.c_ssize_t),
#         ("ob_type", ctypes.c_void_p),
#         ("length", ctypes.c_ssize_t),
#         ("hash", ctypes.c_ssize_t),
#         ("state", ctypes.c_uint),
#         ("wstr", ctypes.c_void_p),
#     ]
#
# def extract_utf16_from_string(py_string):
#     addr = id(py_string)
#     ascii_obj = PyASCIIObject.from_address(addr)
#
#     length = ascii_obj.length
#     state = ascii_obj.state
#
#     kind = (state >> 2) & 0b111
#     compact = (state >> 6) & 1
#     ascii_flag = (state >> 0) & 1
#
#     print(f"[INFO] kind={kind}, compact={compact}, ascii={ascii_flag}, length={length}")
#
#     if not (kind == 1 and compact == 1 and ascii_flag == 0):
#         raise AssertionError("This only works for kind=1, compact=1, ascii=0 strings.")
#
#     # Obliczamy adres danych:
#     offset = ctypes.sizeof(PyASCIIObject)
#     print("offset", offset)
#     print("length", length)
#     data_ptr = addr + offset
#     raw = ctypes.string_at(data_ptr, length * 2)  # 2 bajty na znak
#
#     print(f"[DEBUG] Raw bytes: {raw}")
#     decoded = raw.decode("utf-16le")  # endianność CPython
#     print(f"[RESULT] Decoded string: {decoded}")
#     return decoded, raw
#
#
# s = print_x1.__class__.__name__
# # s = ''.join(print_x1.__class__.__name__)
# # _ = s.encode("utf-16le")  # wymuś alokację .utf8, choć tu nie używamy
#
# # # [RESULT] Decoded string: function
# # raw_bytes_copy = (ctypes.c_char * len(raw)).from_buffer_copy(raw)
# # raw_bytes_copy[0] = b'*'[0]
#
# # Tworzymy bajty znaku 'h' w UTF-16LE
# # new_char = 'h'.encode('utf-16le')  # b'h\x00'
# #
# # size = sys.getsizeof(s)
#
#
#
# # raw with offset
# decoded, raw = extract_utf16_from_string(s)
#
# raw_bytes_copy = (ctypes.c_char * 16).from_buffer_copy(raw)
# raw_bytes_copy[0] = b'*'[0]
# # raw_bytes_copy[15] = b'*'[0]
# # ctypes.memmove(id(raw), raw_bytes_copy, 2)
#
#
#
# bx = bytes()
#
# for b in list(raw_bytes_copy):
#     bx = bx + b
#
# ctypes.memmove(id(s) + 48, bx, len(bx))
# print(s)
# print(print_x1.__class__.__name__)
#
# # for b in list(raw_bytes_copy):
# #     bx = bx + b
# #     break
#
# bf = bytes("F", "utf-16le")
#
# print(id(print_x1.__class__.__name__))
#
# ptr = ctypes.cast(id(print_x1.__class__.__name__), ctypes.c_void_p).value
# print(hex(ptr))
# print(hex(id(print_x1.__class__.__name__)))
#
# # ctypes.memmove(id(print_x1.__class__.__name__) + 48, bf, len(bx))
# # print(print_x1.__class__.__name__)


import ctypes
import sys

Py_ssize_t = ctypes.c_ssize_t

class PyASCIIObject(ctypes.Structure):
    _fields_ = [
        ('ob_refcnt', Py_ssize_t),
        ('ob_type', ctypes.c_void_p),
        ('length', Py_ssize_t),
        ('hash', Py_ssize_t),
        ('state', ctypes.c_uint),
        ('wstr', ctypes.c_void_p),  # zamiast wchar_p — zgodność niskopoziomowa
    ]

class PyCompactUnicodeObject(ctypes.Structure):
    _fields_ = [
        ('_base', PyASCIIObject),
        ('utf8_length', Py_ssize_t),
        ('utf8', ctypes.c_char_p),
        ('wstr_length', Py_ssize_t),
    ]

# Tworzymy przykładowy ciąg znaków
s = "zażółć gęślą jaźń"
utf8_data = s.encode()
utf8_length = len(utf8_data)

bx = bytes()


skip = 1
for b in utf8_data:
    if skip:
        b = bytes("*", "utf-8")
        bx = bx + b
        skip = 0
        continue

    b = bytes(chr(b), "utf-8")
    bx = bx + b

if len(sys.argv) > 1:
    null_terminated = bx + b"\x00"
else:
    null_terminated = utf8_data + b"\x00"
# Obliczamy całkowity rozmiar: struktura + bajty UTF-8 + null
total_size = ctypes.sizeof(PyCompactUnicodeObject) + len(null_terminated)

# Alokujemy blok pamięci
buffer = ctypes.create_string_buffer(total_size)

# Tworzymy strukturę w tym buforze
py_obj = PyCompactUnicodeObject.from_buffer(buffer)

# Ustawiamy dane w strukturze
py_obj._base.length = len("zażółć gęślą jaźń")  # liczba znaków
py_obj.utf8_length = utf8_length
py_obj.wstr_length = len("zażółć gęślą jaźń")

# Obliczamy adres, gdzie zaczynają się dane UTF-8
addr_of_struct = ctypes.addressof(buffer)
addr_of_utf8_data = addr_of_struct + ctypes.sizeof(PyCompactUnicodeObject)

# Kopiujemy dane UTF-8 za strukturę
ctypes.memmove(addr_of_utf8_data, null_terminated, len(null_terminated))

# Ustawiamy pole .utf8 tak, by wskazywało na dane po strukturze
py_obj.utf8 = ctypes.cast(addr_of_utf8_data, ctypes.c_char_p)

# ✅ Odczyt
print("UTF-8 length:", py_obj.utf8_length)
print("UTF-8 data (raw):", py_obj.utf8)
print("UTF-8 decoded:", py_obj.utf8.decode("utf-8"))

