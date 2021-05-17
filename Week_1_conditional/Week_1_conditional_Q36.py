"""WAPTP true if there is an equal number of x's and o's present in the string, otherwise print false"""

s = "xxxxxxxxxxooooooooooo"

c = 0
i = 0
while i < len(s):
    if s[i] == "x":
        c += 1
    else:
        c -= 1
    i += 1
if c == 0:
    print("True")
else:
    print("False")
