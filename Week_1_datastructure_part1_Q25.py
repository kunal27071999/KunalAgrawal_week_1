"""25. WAP to get average of integers present in array"""

from array import *
sum = 0
a = array('i',[1,2,3,4,5])

for i in a:
    sum+=i
print(sum/len(a))