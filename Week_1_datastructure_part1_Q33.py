"""33. WAP to split the array and add the first part to the end"""

from array import *

a = array('i',[1,2,3,4,5,6])
first = [a[i] for i in range(0,len(a)//2)]
second = [a[i] for i in range(len(a)//2, len(a))]
print(second + first)

