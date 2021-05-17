"""41. Next Palindrome
Have the function NextPalindrome(num) take the num parameter being passed and return the next largest palindromic number. The input can be any positive integer. For example: if num is 24, then your program should return 33 because that is the next largest number that is a palindrome.
Examples
Input: 2
Output: 3
Input: 180
Output: 181"""

def nextPalindrome(num):
    rev = 0
    temp = 0
    while num > 0:
        rev = num % 10
        temp = temp * 10 + rev
        num = num//10
    return temp



n = 2
while True:
    n += 1
    if n == nextPalindrome(n):
        print(n)
        break

