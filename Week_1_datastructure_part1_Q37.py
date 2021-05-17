"""37. WAP to print output of below slicing options
Input array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Operations
	1. a[3:8]
	2. a[5:]
	3. a[:]"""

from array import *

a = array('i',[1,2,3,4,5,6,7,8,9,10])

print(a[3:8])
print(a[5:])
print(a[:])
