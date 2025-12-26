"""1 - create string text (S1 object)
2 - generate raw bytes object related to S1 string (raw_bytes object)
3 - generate copy object of raw bytes (raw_bytes_copy object)
4 - modify raw_bytes_copy object bytes
5 - replace S1-related raw bytes object (raw_bytes)
6 - print changed S1 string object
"""


# 1
S1 = "Text to be modified."
import ctypes


# Raw bytes, header + data + what left
# s1_addreess = id(S1)
# import sys
# len_S1_extended = sys.getsizeof(S1) + 20
# len_size = 96
# raw_bytes = ctypes.string_at(id(S1), len_size)

# # print(raw_bytes)
#
# for i in range(95):
#     print(raw_bytes[i], chr(raw_bytes[i]))
#     if  chr(raw_bytes[i]) == "T":
#         print("offset", i)
#         break

# 2
raw_bytes = ctypes.string_at(id(S1), 96)
# 3
raw_bytes_copy = (ctypes.c_char * len(raw_bytes)).from_buffer_copy(raw_bytes)


# 4
raw_bytes_copy[45] = b'-'[0]
raw_bytes_copy[46] = b'>'[0]
raw_bytes_copy[47] = b' '[0]
raw_bytes_copy[48] = b'*'[0]
raw_bytes_copy[49] = b't'[0]
raw_bytes_copy[50] = b'e'[0]
raw_bytes_copy[51] = b'x'[0]
raw_bytes_copy[52] = b't'[0]
raw_bytes_copy[53] = b' '[0]
raw_bytes_copy[54] = b'w'[0]
raw_bytes_copy[55] = b'a'[0]
raw_bytes_copy[56] = b's'[0]
raw_bytes_copy[57] = b'*'[0]

# 5
# ctypes.memmove(s1_addreess, raw_bytes_copy, len(raw_bytes_copy))
ctypes.memmove(id(S1), raw_bytes_copy, len(raw_bytes_copy))

# 6
print(S1)
