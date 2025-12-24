

S1 = "Text to be modified."

import ctypes

# Raw bytes, header + data + what left
s1_addreess = id(S1)
raw_bytes = ctypes.string_at(s1_addreess, 96)
print(raw_bytes)

for i in range(95):
    print(raw_bytes[i], chr(raw_bytes[i]))
    if  chr(raw_bytes[i]) == "T":
        print("offset", i)
        break

raw_bytes_copy = (ctypes.c_char * len(raw_bytes)).from_buffer_copy(raw_bytes)


raw_bytes_copy[48] = b'*'[0]
raw_bytes_copy[49] = b't'[0]
raw_bytes_copy[50] = b'e'[0]
raw_bytes_copy[51] = b'x'[0]
raw_bytes_copy[52] = b't'[0]
raw_bytes_copy[53] = b' '[0]
raw_bytes_copy[54] = b'w'[0]
raw_bytes_copy[55] = b'a'[0]
raw_bytes_copy[56] = b's'[0]
raw_bytes_copy[57] = b' '[0]


ctypes.memmove(s1_addreess, raw_bytes_copy, len(raw_bytes_copy))
# print(S1)
# print(s1_addreess == id(S1))
