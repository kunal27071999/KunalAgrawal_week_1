"""WAPTP sum of first n natural numbers"""
"""20. WAPTP cube of first n numbers"""

sum = 0
cube = 0
n= 3
for i in range(1, n+1):
    sum = sum + i
    cube = cube + (i*i*i)
print(sum)
print(cube)