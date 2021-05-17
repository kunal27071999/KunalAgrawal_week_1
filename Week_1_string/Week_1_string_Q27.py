""" WAP to sort characters of string, first alphabets symbols followed by numeric valuesEx
str1 = "Q9W3E81"
Output will be EQW1389"""



str1 = "Q9W3E81"
num = []
string =[]
l = list(str1)
for i in l:
    if i.isdigit():
        int(i)
        num.append(i)
    else:
        string.append(i)

print("".join(sorted(string)+sorted(num)))







