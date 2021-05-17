"""35. WAP to check if given array is Monotonic"""


def isMono(a):
    return (all(a[i] <= a[i + 1] for i in range(len(a) - 1)) or
            all(a[i] >= a[i + 1] for i in range(len(a) - 1)))


a = [6, 5, 4, 4]
print(isMono(a))
