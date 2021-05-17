"""WAP to print swap two numbers without using the third variable"""

a = 1
b = 2

print("Before swap :", a, b)

a = a + b
b = a - b
a = a - b

print("After swap :", a, b)
