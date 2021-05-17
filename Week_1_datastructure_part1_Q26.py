"""26. Create an array of size 10 and insert new element at position 3 and 7 and update the position 2"""

from array import *
a = array('i',[1,2,3,4,5,6,7,8,9,10])

a.insert(3,11)
print(a)
a.insert(7,12)
a[2] = 13
print(a)
