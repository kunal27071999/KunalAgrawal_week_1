"""12. WAP to print biggest of three numbers"""

num2 = 2000
num1 = 100
num3 = 300000

if num1 > num2:
    if num1 > num3:
        print("num :", num1)
    else:
        print("num :", num3)
elif num2 > num1:
    if num2 > num3:
        print("num :", num2)
    else:
        print("num :", num3)
