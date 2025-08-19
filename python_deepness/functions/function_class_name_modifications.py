import ctypes
import sys

# def call(args, kwargs):
#     print("fake call print")
#     args[0](*args[1:], **kwargs)
#
#
#
def print_x1():
    print("x1")


# print_x1.__call__ = call

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
        # ('utf8_length', Py_ssize_t),
        # ('utf8', ctypes.c_char_p),
        # ('wstr_length', Py_ssize_t),
    ]



def print_raw_bytes_string_settings(testval, obj):
    addr = id(obj)
    ascii_obj = PyASCIIObject.from_address(addr)
    length = ascii_obj.length
    state = ascii_obj.state

    compact = (state >> 6) & 1
    ascii_flag = (state >> 0) & 1
    kind = (state >> 2) & 7
    interned = (state >> 28) & 0b11
    interned2 = (state >> 7) & 0b11,

    # print(locals())
    if compact and ascii_flag:
        # Compact ASCII - 1 bajt na znak
        data_addr = addr + ctypes.sizeof(PyASCIIObject)
        raw_chars = (ctypes.c_char * length).from_address(data_addr)
        # return bytes(raw_chars)
        print(locals())
    else:
        print(locals())





s0 = "chwila"
s1 = "function"
s2 = ''.join(print_x1.__class__.__name__)
s3 = print_x1.__class__.__name__
# s3 = ''.join(print_x1.__class__.__name__)  # lub str(...)
print()
print(id(print_x1.__class__.__name__))  # nowy adres
print(id(s3))  # nowy adres
print(id(s2))  # nowy adres
print(id(s1))  #
print(id(sys.intern("function")))
#
#
# print_raw_bytes_string_settings("s0", s0)
# print_raw_bytes_string_settings("s1", s1)
# print_raw_bytes_string_settings("s2", 2)
# print_raw_bytes_string_settings("print_x1.__class__.__name__", print_x1.__class__.__name__)


def emulate_PyCompactUnicodeObject(s):
    s_utf8_data = s.encode("utf-8")
    s_utf8_length = len(s.encode("utf-8"))

    s__utf8data_with_null = b'*unction' + b"\x00"


    # Obliczamy całkowity rozmiar: struktura + bajty UTF-8 + null
    print(ctypes.sizeof(PyCompactUnicodeObject))
    total_size = ctypes.sizeof(PyCompactUnicodeObject) + len(s__utf8data_with_null)
    # total_size2 = ctypes.sizeof(PyASCIIObject) + len(s__utf8data_with_null)

    # Alokujemy blok pamięci
    buffer = ctypes.create_string_buffer(total_size)

    print("[sys.getsizeof] total_size:", sys.getsizeof(s))
    print("[PyCompactUnicodeObject] total_size:", total_size)
    # Tworzymy strukturę w tym buforze
    py_obj = PyCompactUnicodeObject.from_buffer(buffer)

    # Ustawiamy dane w strukturze
    py_obj._base.length = len(s)  # liczba znaków
    py_obj.utf8_length = s_utf8_length
    py_obj.wstr_length = len(s)

    # Obliczamy adres, gdzie zaczynają się dane UTF-8
    addr_of_struct = ctypes.addressof(buffer)
    addr_of_utf8_data = addr_of_struct + ctypes.sizeof(PyCompactUnicodeObject)

    # Kopiujemy dane UTF-8 za strukturę
    ctypes.memmove(addr_of_utf8_data, s__utf8data_with_null, len(s__utf8data_with_null))

    # Ustawiamy pole .utf8 tak, by wskazywało na dane po strukturze
    py_obj.utf8 = ctypes.cast(addr_of_utf8_data, ctypes.c_char_p)


emulate_PyCompactUnicodeObject(s0)
emulate_PyCompactUnicodeObject(s1)
emulate_PyCompactUnicodeObject(s2)
emulate_PyCompactUnicodeObject(s3)
print("[sys.getsizeof**] total_size:", sys.getsizeof(print_x1.__class__.__name__))


print()
print()

def read_utf8_from_compact_unicode(obj):
    addr = id(obj)
    ascii_obj = PyASCIIObject.from_address(addr)
    offset = ctypes.sizeof(PyASCIIObject)
    # Dane UTF-8 są tuż za strukturą
    raw = (ctypes.c_char * ascii_obj.length).from_address(addr + offset)
    return bytes(raw)

print(read_utf8_from_compact_unicode(s0))
print(read_utf8_from_compact_unicode(s1))
print(read_utf8_from_compact_unicode(s2))
print(read_utf8_from_compact_unicode(s3))
print(read_utf8_from_compact_unicode(print_x1.__class__.__name__))


# Raw bytes, header + data + what left
s1_addreess = id(print_x1.__class__.__name__)
s1_addreess = id(s1)

def find_offset(sx):
    size_b = sys.getsizeof(sx)
    raw_bytes = ctypes.string_at(id(sx), size_b)

    for i in range(size_b):
        # print(raw_bytes[i], chr(raw_bytes[i]))
        if  chr(raw_bytes[i]) == "f":
            print("offset", i, size_b)
            return i
    else:
        print("offset could not be found")
        return None

offsets = []
_ = find_offset(s0)
offsets.append(_)
_ = find_offset(s1)
offsets.append(_)
_ = find_offset(s2)
offsets.append(_)
_ = find_offset(s3)
offsets.append(_)
_ = find_offset(print_x1.__class__.__name__)
offsets.append(_)

print(offsets)


raw_bytes0 = ctypes.string_at(id(s0), sys.getsizeof(s0))
raw_bytes1 = ctypes.string_at(id(s1), sys.getsizeof(s1))
raw_bytes2 = ctypes.string_at(id(s2), sys.getsizeof(s2))
raw_bytes3= ctypes.string_at(id(s3), sys.getsizeof(s3))
raw_bytes4 = ctypes.string_at(id(print_x1.__class__.__name__), sys.getsizeof(print_x1.__class__.__name__))


def extract_text_bytes(obj):
    addr = id(obj)
    ascii_obj = PyASCIIObject.from_address(addr)

    compact = (ascii_obj.state >> 6) & 1
    ascii_flag = (ascii_obj.state >> 0) & 1
    kind = (ascii_obj.state >> 2) & 7
    length = ascii_obj.length

    offset = ctypes.sizeof(PyASCIIObject)

    # tylko dla compact strings!
    raw_ptr = addr + offset

    if ascii_flag:
        print("A1")
        raw = (ctypes.c_char * length).from_address(raw_ptr)
        return bytes(raw).decode("ascii"), raw
    elif kind == 1:
        print("A2")
        print(length)
        raw = (ctypes.c_ubyte * length).from_address(raw_ptr)
        # print(bytes(raw).decode("latin1"), raw)
        #
        # raw_bytes = bytes(raw)
        # null_pos = raw_bytes.find(b'\x00')
        # if null_pos != -1:
        #     text = raw_bytes[:null_pos].decode("latin1")  # albo "utf-8" jeśli wiesz, że jest utf8
        # else:
        #     text = raw_bytes.decode("latin1")
        # print(text)
        #
        # def c_string_from_address(addr, max_length=1024):
        #     """
        #     Odczytuje C-string (null-terminated) spod podanego adresu pamięci.
        #     max_length - maksymalna długość do odczytu, aby nie czytać za dużo.
        #     """
        #     raw = (ctypes.c_ubyte * max_length).from_address(addr)
        #     raw_bytes = bytes(raw)
        #     null_pos = raw_bytes.find(b'\x00')
        #     if null_pos == -1:
        #         # Nie znaleziono końca stringa, bierzemy max_length
        #         null_pos = max_length
        #     return raw_bytes[:null_pos].decode("latin1")  # lub "utf-8" jeśli jesteś pewien
        #
        # # Przykład użycia:
        #
        # address = id(print_x1.__class__.__name__)  # adres stringa
        # text = c_string_from_address(address, max_length=100)
        # print("Odczytany string:", text)

        return bytes(raw).decode("latin1"), raw  # UCS-1 == Latin1
    elif kind == 2:
        print("A3")
        raw = (ctypes.c_uint16 * length).from_address(raw_ptr)
        return "".join(chr(c) for c in raw), raw
    elif kind == 4:
        print("A4")
        raw = (ctypes.c_uint32 * length).from_address(raw_ptr)
        return "".join(chr(c) for c in raw), raw
    else:
        raise RuntimeError("Unknown kind")

#
print(sys.getsizeof(print_x1.__class__.__name__))  # większy string (kind=4)
string_text, raw_ = extract_text_bytes(print_x1.__class__.__name__)
# breakpoint()
print(string_text, raw_)  # powinien zwrócić oryginalny tekst

print()


raw_bytes = [raw_bytes0, raw_bytes1, raw_bytes2, raw_bytes3, raw_bytes4]
for rw in raw_bytes:
    print(rw)
print()

bx = None

def modify_str(raw_byte_str, str_val, exception_str=False):
    str_name = "None"
    for name, val in globals().items():
        if exception_str:
            str_name = exception_str
            break

        if val == str_val and id(str_val) == id(str_val):
            # print(f"Nazwa zmiennej to: {name}")
            str_name = name
            break

    raw_bytes_copy = (ctypes.c_char * len(raw_byte_str)).from_buffer_copy(raw_byte_str)
    # print(len(raw_byte_str))
    # print(len(raw_bytes_copy), raw_bytes_copy)
    # print(str_val)
    l_raw_bytes_copy = list(raw_bytes_copy)

    global bx
    bx = bytes()

    for i, b in enumerate(l_raw_bytes_copy):
        replacing_word = "*FUNCT*********"
        if i > 47 and i < 57:
            letter = f"{replacing_word[i-48]}"
            bx = bx + bytes(letter, "utf-8")

    # print(bx, len(bx))
    # print(l_raw_bytes_copy)

    str_old_bak = "".join(str_val)
    # print(raw_bytes_copy[48])
    # raw_bytes_copy[48] = b'*'
    # raw_bytes_copy[49] = b'*'[0]
    # raw_bytes_copy[50] = b'*'[0]
    # raw_bytes_copy[51] = b'*'[0]
    # raw_bytes_copy[52] = b'*'[0]
    # print(l_raw_bytes_copy)

    print(str_name, ":", sep="")
    print(str_val)
    print(id(str_val))
    ret = ctypes.memmove(id(str_val) + 48, bx, 7)
    print(id(str_val))
    print(ret)
    print(id(str_val))
    print(str_val)
    print()


modify_str(raw_bytes0, s0)
modify_str(raw_bytes1, s1)
modify_str(raw_bytes2, s2)
modify_str(raw_bytes3, s3)
modify_str(raw_bytes4, print_x1.__class__.__name__, exception_str="print_x1.__class__.__name__")

print("Is string text interned?")
print(" s1:function is interned"
      if id(s1) == id(sys.intern("function"))
      else " s1:function is not interned"
)
print(" s2:function is interned"
      if id(s2) == id(sys.intern("function"))
      else " s2:function is not interned"
)
print(" s3:function is interned"
      if id(s3) == id(sys.intern("function"))
      else " s3:function is not interned"
)

if id(print_x1.__class__.__name__) == id(sys.intern("function")):
    print(" print_x1.__class__.__name__:function is interned")
else:
    print(" print_x1.__class__.__name__:function is not interned")
print()


print("It works?")
print(s1)
print(s2)
print(s3)
print(print_x1.__class__.__name__)
# ret = ctypes.memmove(id(print_x1.__class__.__name__) + 48, bx, 9)

#
# def read_utf8_from_compact_unicode(obj):
#     addr = id(obj)
#     ascii_obj = PyASCIIObject.from_address(addr)
#     offset = ctypes.sizeof(PyASCIIObject)
#     # Dane UTF-8 są tuż za strukturą
#     raw = (ctypes.c_char * ascii_obj.length).from_address(addr + offset)
#     print(ascii_obj, offset, raw, len(raw))
#
#     print("raw:", raw)
#     print("bytes(raw):", bytes(raw))
#     print("list(raw):", list(raw))
#     ctypes.memmove(id(print_x1.__class__.__name__) + 48, bytes(raw), len(raw))
#
#
#
# # print()
# # print()
# # # read_utf8_from_compact_unicode(print_x1.__class__.__name__) # Segmentation fault (core dumped)
# #
# # size_ = sys.getsizeof(print_x1.__class__.__name__)
# # # 57
# #
# # # print(id(print_x1.__class__.__name__))
# # # id_ = ctypes.memmove(id(print_x1.__class__.__name__) + 48, bytes("x", "utf-8"), 1)
# # # print(id_)
# # # print(id(print_x1.__class__.__name__))
# #
# #
# #
# # raw = (ctypes.c_ubyte * size_).from_address(id(print_x1.__class__.__name__))
# # raw_bytes_copy = (ctypes.c_ubyte * size_).from_buffer_copy(raw)
# # raw_bytes_copy[48] = bytes("x", "latin1")[0]
# # # raw_bytes_copy[48] = b'*'[0]
# # print(id(print_x1.__class__.__name__))
# # where = ctypes.memmove(id(print_x1.__class__.__name__), raw_bytes_copy, size_)
# # print(where)
# # print(id(print_x1.__class__.__name__))
# # print(print_x1.__class__.__name__)
# #
# # print()
# #
# # where_b = ctypes.string_at(where, 57)
# # print("where_b:", where_b)
# # print(where_b.decode("latin1"))
# # print()
# # print()
# # print()
# #
# #
# # import ctypes
# #
# # # Weź typ obiektu — np. print → jego klasa to <class 'builtin_function_or_method'>
# # cls = print_x1.__class__
# # addr_cls = id(cls)
# #
# # # Zdefiniuj strukturę z odpowiednim polem na tp_name
# # class PyTypeObject(ctypes.Structure):
# #     _fields_ = [
# #         ("ob_refcnt", ctypes.c_ssize_t),
# #         ("ob_type", ctypes.c_void_p),
# #         ("ob_size", ctypes.c_ssize_t),
# #         ("tp_name", ctypes.c_char_p),  # const char *
# #     ]
# #
# # # Wczytaj strukturę z pamięci
# # type_obj = PyTypeObject.from_address(addr_cls)
# #
# # # Odczytaj tp_name jako bytes i jako string
# # tp_name_ptr = type_obj.tp_name
# # print(f"tp_name_ptr: {tp_name_ptr}")
# # print("tp_name bytes:", ctypes.string_at(tp_name_ptr))      # raw bytes
# # print("tp_name str  :", ctypes.string_at(tp_name_ptr).decode())  # decoded string
# #
# # print(id(type_obj))
# # print(id(tp_name_ptr))


# Widać, że modyfikacja print_x1.__class__.__name__ jest dość trudna:
#
# 1. __name__ to nie zwykły prosty string w Pythonie
#    __name__ to atrybut typu str, ale ten string jest może być internowany i zarządzany przez CPythona (w przypadku print_x1.__class__.__name__ akurat nie).
#
#    Python utrzymuje wiele mechanizmów optymalizacji dla takich często używanych stringów (np. internowanie, immutable memory).
#    Wiele obiektów może wskazywać na ten sam obiekt string (referencje).


# 2. Adres id(print_x1.__class__.__name__) wskazuje na strukturę Pythona, nie tylko na raw string
#    id() zwraca adres obiektu Pythonowego.
#    Natomiast, w pamięci ten obiekt to struktura PyUnicodeObject (lub jej warianty jak PyASCIIObject, PyCompactUnicodeObject).
#    Sam tekst:
#     - jest przechowywany w polu tej struktury,
#     - często nie pod tym samym adresem co struktura
#     - albo jest zarządzany wewnętrznie.
#
# Modyfikacja pamięci pod adresem id(obj) może więc modyfikować strukturę, a nie bezpośrednio ciąg znaków.


# 3. Ciągi znaków w Pythonie są niemodyfikowalne (immutable)
#    Stringi w Pythonie są niemodyfikowalne, więc bezpośrednia zmiana ich pamięci może powodować:
#     - Nieprzewidywalne zachowania,
#     - Wiele innych obiektów wskazujących na ten sam string pozostanie niezmienionych,
#     - Konflikty z mechanizmami zarządzania pamięcią i cache.


# 4. Wewnętrzne formaty i kodowanie znaków są złożone
#    PyUnicodeObject może przechowywać tekst w różnych formatach (1, 2 lub 4 bajtów na znak),
#    Nie zawsze jest to prosta tablica bajtów UTF-8,
#    Złożona struktura i kodowanie wymaga dokładnej znajomości implementacji CPythona i odpowiedniej struktury ctypes.


# 5. memmove zmienia bajty w pamięci, ale Python może mieć cache lub kopie
#    Nawet jeśli fizycznie zmienisz bajty pod adresem, Python może korzystać z cache lub innej reprezentacji,
#    Obiekt str może być współdzielony, więc zmiany mogą nie mieć oczekiwanego efektu,
#    Interpreter może nie zauważyć zmiany lub korzystać z oryginalnej wartości.


# 6. id(obj) to adres całego obiektu, niekoniecznie danych znakowych
#    Struktura obiektu i dane znakowe mogą być pod różnymi adresami,
#    Trzeba dokładnie odczytać, gdzie jest pole z danymi znakowymi i modyfikować je tam, a nie samą strukturę.

# Podsumowując
#    Modyfikowanie print_x1.__class__.__name__ bezpośrednio w pamięci to zabawa z:
#       wewnętrznym formatem PyUnicodeObject,
#       immutable stringiem i optymalizacjami Pythona.

# To nie jest prosta tablica bajtów pod adresem id(), a złożona, zarządzana struktura z kilkoma warstwami abstrakcji i optymalizacji.

def dump_ob_type(x):
    addr = id(x)
    ob_type_addr = int.from_bytes(ctypes.string_at(addr + 8, 8), 'little')
    print(f"{repr(x):<12} | ob_type: {hex(ob_type_addr)} == id(type(x)): {hex(id(type(x)))} | same? {ob_type_addr == id(type(x))}")


def read_compact_ascii_str_data(obj: str, length=16):
    from ctypes import string_at
    addr = id(obj)
    inline_offset = 64  # dla CPython compact ascii
    return string_at(addr + inline_offset, length)

s = print_x1.__class__.__name__  # 'function'
raw = read_compact_ascii_str_data(s, len(s))
print("RAW:", raw)
print("Decoded:", raw.decode('latin-1'))
# print("Decoded:", raw.decode('ascii'))


def is_compact_ascii_string(obj):
    addr = id(obj)
    # offset do pola 'state' to 4 bajty (Py_ssize_t length) + 4 bajty (hash) = 8 bajtów po PyObject_HEAD
    # W 64bit PyObject_HEAD to 16 bajtów, więc offset pola state jest 16 + 8 = 24 bajty od adresu obiektu
    # W praktyce dla CPython 3.8+ offset pola state = 24
    state = ctypes.c_uint.from_address(addr + 24).value
    print(state)
    compact = (state & 0x40) != 0
    ascii_flag = (state & 0x80) != 0
    return compact, ascii_flag

s = print_x1.__class__.__name__
compact, ascii_flag = is_compact_ascii_string(s)
print(f"compact: {compact}, ascii: {ascii_flag}")

# ale ...
state = ctypes.c_uint.from_address(id(print_x1.__class__.__name__) + 24).value
compact = (state & 0x40) != 0
ascii_flag = (state & 0x80) != 0
# ..  'compact': True, 'ascii_flag': True, 'state': 4294967295}


statex = ctypes.c_uint.from_address(id(print_x1.__class__.__name__) + 32).value
print(f"State: {statex:#010x}")
compact = (statex & 0x40) != 0
ascii_flag = (statex & 0x80) != 0
print(f"compact: {compact}, ascii: {ascii_flag}")

addr = id(print_x1.__class__.__name__)
state = ctypes.c_uint.from_address(addr + 24).value
compact = (state & 0x40) != 0
ascii_flag = (state & 0x80) != 0
print(state, compact)
if not (compact and ascii_flag):
    raise ValueError("To nie jest compact ascii string")
# offset 64 bajty to dane
length = len(print_x1.__class__.__name__)
print(length)
x1 = ctypes.string_at(addr + 64, length)
print(x1)
x2 = ctypes.string_at(addr + 56, length)
print(x2)


s = "function"  # ręcznie utworzony
addr = id(s)
state = ctypes.c_uint.from_address(addr + 24).value
compact = (state & 0x40) != 0
ascii_flag = (state & 0x80) != 0
print(f"state: {state:#x}, compact: {compact}, ascii: {ascii_flag}")
x = ctypes.string_at(addr + 64, len(s))
print(x)
