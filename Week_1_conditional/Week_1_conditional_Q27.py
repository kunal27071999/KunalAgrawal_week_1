"""WAPTP all prime numbers within a range 1 to 500"""

n = 500
flag = 0
for i in range(1, n+1):
    if i == 1:
        continue
    flag = 1

    if i > 1:
        for num in range(2, i//2 + 1):
            if i % num == 0:
                flag = 0
                break
        if flag == 1:
            print(i, end=" ")
