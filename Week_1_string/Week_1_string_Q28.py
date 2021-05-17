"""WAP to print the character number of time given in the strings next index
Ex: a5b2c3
output will be : aaaaabbccc"""

str1 = "a5b2c3"
final = []
num = []
string =[]
l = list(str1)
for i in l:
    if i.isdigit():
        int(i)
        num.append(i)
    else:
        string.append(i)
for i in num:
    a =i
    while(int(num[i]) > 0):
        final.append(string[a])
        num[i]-=1
print(final)