"""WAP to find the missing number in a given array of numbers between 20 to 50"""

from array import *

a = array('i',[20 ,30 ,38,25,24,23,50])

for i in range(20,50):
    if i not in a:
        print(i, end= " ")
