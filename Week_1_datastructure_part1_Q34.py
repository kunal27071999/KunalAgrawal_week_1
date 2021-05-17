"""4. WAP to find reminder of array multiplication divided by n"""

from array import *
mul = 1
a =array('i', [1,2,3,4,3])
for i in a:
    mul*=i
print(mul % len(a))
