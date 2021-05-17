"""11. WAP to print whether entered number if int, float or complex"""

num = 10+10j
if type(num) == int:
    print("integer number")
elif type(num) == float:
    print("decimal number")
elif type(num) == complex:
    print("complex number")
else:
    pass
