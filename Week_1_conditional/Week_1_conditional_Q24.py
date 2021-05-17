"""24. WAPTP fibonacci series of n"""


n = 10
n1 = 0
n2 = 1
if (n < 1):
    pass

print(n1, end=" ")
for x in range(1, n):
    print(n2, end=" ")
    nextNum = n1 + n2
    n1 = n2
    n2 = nextNum
