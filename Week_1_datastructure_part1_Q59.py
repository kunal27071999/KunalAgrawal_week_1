"""59. WAP to get median of two sorts arrays"""

from array import *

a = [1,2,3,4,5,6,8,9]
b = [3,34,5,6,7,89,9]

c = a + b
c.sort()

n =len(c)
if n % 2 != 0:
    print("median", float(c[int(n/2)]))
else:
    print("median", float((c[int((n - 1) / 2)] + c[int(n / 2)]) / 2.0))
