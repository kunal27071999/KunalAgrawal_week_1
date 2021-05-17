"""13. WAP to find substring in backword direction using rfind() and rindex()
str1 = "demo"
str2 = "the python demo is scheduled"""

# USING FIND
str1 = "demo"
str2 = "the python demo is demo scheduled"

print(str2.rfind(str1))
#USING INDEX
ch = "demo"
ch1 = "the python demo is scheduled"

pos = ch1.rindex(ch)
print(pos)
