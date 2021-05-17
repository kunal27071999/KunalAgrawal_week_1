"""2. WAP to get the type, address of below variable and print them
a = 10
b = 3.124
c = "35"
d = "4.2"
e = "s1 """


num = [10, 3.124, "35", "4.2", "s1"]

for i in num:
    print(i, type(i), id(i))
