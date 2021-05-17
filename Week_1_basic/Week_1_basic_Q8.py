"""8. Casting, write a programe to cast and print all the below variables into
 int, float, complex, bool and string. Mention the reason wherever the conversion did not happen.
a = 10
b = 3.124
c = "35"
d = "4.2"
e = "s1"
f = True
g = "0B1111"
h.  "five"
i. 0 """

convertList = [10, 3.124, "35"]
d = "4.2"
e = "s1"
f = True
g = "0B1111"
h = "five"
num = 0

for i in convertList:
    print(i, "in int :", int(i))
    print(i, " in decimal: ", float(i))
    print(i, " in complex ", complex(i))
    print(i, "in bool", bool(i))
    print(i, "in sting", str(i))


# print(d, "in int :", int(d)) cannot be type casted because integer value cannot contain float
# to convert it 1st typecast in float then int.
print(d, " in decimal: ", float(d))
print(d, " in complex ", complex(d))
print(d, "in bool", bool(d))
print(d, "in sting", str(d))

# print(e, "in integer : ", int(e)) to convert the string in int,float or complex it must be in base 10(0-9)
# print(e, " in decimal: ", float(e))
# print(e, " in complex ", complex(e))
print(e, "in bool", bool(e))
print(e, "in sting", str(e))

print(f, " in integer : ", int(f))
print(f, " in decimal: ", float(f))
print(f, " in complex ", complex(f))
print(f, "in bool", bool(f))
print(f, "in sting", str(f))

# print(g, " in integer : ", int(g))
# print(g, " in decimal: ", float(g))
# print(g, " in complex ", complex(g))
print(g, "in bool", bool(g))
print(g, "in sting", str(g))

# print(h, " in integer : ", int(h))
# print(h, " in decimal: ", float(h))
# print(h, " in complex ", complex(h))
print(h, "in bool", bool(h))
print(h, "in sting", str(h))

print(num, " in integer : ", int(num))
print(num, " in decimal: ", float(num))
print(num, " in complex ", complex(num))
print(num, "in bool", bool(num))
print(num, "in sting", str(num))
