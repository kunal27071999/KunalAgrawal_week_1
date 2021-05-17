"""22. WAP to get the current memory address and the length in elements of the buffer used to hold an array's
 contents and also find the size of the memory buffer in bytes
"""

from array import *
a = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a.buffer_info())
print(a.buffer_info()[1] * a.itemsize)

