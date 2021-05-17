"""WAP to search en element 7 in the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""

from array import *
find = 7
a = array('i',[1,2,3,4,5,6,7,8,9,10])

for i in a:
    if find == a[i]:
        print(a[i])
        break
