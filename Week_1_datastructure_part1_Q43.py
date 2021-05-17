"""43. WAP to Find the mean and median of an unsorted array."""

from array import *

a = array('i',[1,2,3,4,5,6,8,9])
sum = 0
for i in range(len(a)):
    sum+=a[i]

print("mean",sum/len(a))

sorted(a)
n =len(a)
if n % 2 != 0:
    print("median", float(a[int(n/2)]))
else:
    print("median", float((a[int((n - 1) / 2)] + a[int(n / 2)]) / 2.0))
