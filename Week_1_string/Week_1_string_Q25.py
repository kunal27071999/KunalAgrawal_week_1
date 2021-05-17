"""25. WAPTP characters from odd position in one lineand even positions in second line"""

even = []
odd = []
for i in range(1,10):
    if i %2 != 0:
        odd.append(i)
    else:
        even.append(i)

print(odd,even)

