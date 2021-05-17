"""19. WAP to create an array of 10 integers and display the array items. Access individual element through indexes."""

from array import *

array_num = array('i', [1,2,3,40,50])
for i in array_num:
    print(i)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(a)):
    print(a[i])
