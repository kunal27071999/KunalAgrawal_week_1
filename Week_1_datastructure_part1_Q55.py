"""55. WAP to find whether given number x appears more than n/2 times in a sorted array of size n"""

a = [1,2,3,4,5,6,7,8,9,1,1]
a.sort()
num = 1
count = 0
for i in a:
    if num == a[i]:
        count+=1
if count > len(a)/2:
    print("appeared more than n/2")
else:
    print("not appeared more than n/2")