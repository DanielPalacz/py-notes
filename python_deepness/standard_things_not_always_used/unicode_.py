import sys


s_ = ""
s1 = "a"
s2 = "ab"
s3 = "abc"
s4 = "abcd"
sx = "𐍈"

print("Pure str review (Unicode signs, code points):")
print("\t", "s_ size:", f" - {s_!r}     - ", sys.getsizeof(s_), "bytes")
print("\t", "s1 size:", f" - {s1!r}    - ", sys.getsizeof(s1), "bytes")
print("\t", "s2 size:", f" - {s2!r}   - ", sys.getsizeof(s2), "bytes")
print("\t", "s3 size:", f" - {s3!r}  - ", sys.getsizeof(s3), "bytes")
print("\t", "s4 size:", f" - {s4!r} - ", sys.getsizeof(s4), "bytes")
print("\t", "sx size:", f" - {sx!r}    - ", sys.getsizeof(sx), "bytes")


print()

sb_ = s_.encode("utf-8")
sb1 = s1.encode("utf-8")
sb2 = s2.encode("utf-8")
sb3 = s3.encode("utf-8")
sb4 = s4.encode("utf-8")
sbx = sx.encode("utf-8")

print("Encoded str review (bytes, utf-8):")
print("\t", "sb_ size:", f" - {sb_}\t\t  - ", sys.getsizeof(sb_), "bytes,", f"[{repr(s_)}]")
print("\t", "sb1 size:", f" - {sb1}\t\t  - ", sys.getsizeof(sb1), "bytes,", f"[{s1}]")
print("\t", "sb2 size:", f" - {sb2}\t\t  - ", sys.getsizeof(sb2), "bytes,", f"[{s2}]")
print("\t", "sb3 size:", f" - {sb3}\t\t  - ", sys.getsizeof(sb3), "bytes,", f"[{s3}]")
print("\t", "sb4 size:", f" - {sb4}\t\t  - ", sys.getsizeof(sb4), "bytes,", f"[{s4}]")
print("\t", "sbx size:", f" - {sbx} - ", sys.getsizeof(sbx), "bytes,", f"[{sx}]")

print("\nReminder:")
print("\t * Strings (str objects) in Python3 are implemented as Unicode code points - chr/ord built-in functions can be used.")
print("\t * To have bytes representation one must to use 'str_object.encode(\"ENCODING_SYSTEM\")' - ENCODING_SYSTEM can be fe \'utf-8\'")
