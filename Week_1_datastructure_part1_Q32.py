"""32. WAP to rotate an array. Ex. Input array [1, 2, 3, 4, 5, 6, 7] Output [7, 6, 5, 4, 3, 2, 1]"""

from array import *

a = array('i',[1,2,3,4,5])
rotate = a[0]
for i in range(0,len(a)-1):
    a[i]=a[i+1]
a[len(a)-1]=rotate
print(a)
#output array('i', [2, 3, 4, 5, 1])