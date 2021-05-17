"""28. WAP to reverse a given integer number 23564"""

num = 23564
rev = 0
while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10
print(rev)
