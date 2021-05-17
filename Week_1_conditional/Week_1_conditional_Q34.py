"""4. WAP to calculate GCD and LCM"""


def findGCD(a, b):
    if (b == 0):
        return a;
    else:
        return findGCD(b, a % b)


num1 = 2
num2 = 10
gcd = findGCD(num1, num2)
print(gcd)
lcm = (num1 * num2) // gcd
print(lcm)