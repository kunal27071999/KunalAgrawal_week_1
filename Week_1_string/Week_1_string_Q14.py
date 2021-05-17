"""WAP to display all positions of substing in given string
str1 = "ababadbabdfabefbabab"
str2 = "ab"""

str1 = "ababadbabdfabefbabab"
str2 = "ab"

for i in range(len(str1)):
    if str1.startswith(str2,i):
        print(i)

