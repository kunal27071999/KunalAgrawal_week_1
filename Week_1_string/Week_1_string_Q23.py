""" WAP to print the reverse order of words from statement "Chistats is established in the 2017 and today we are celebrating 4th birthday"""

txt = "Chistats is established in the 2017 and today we are celebrating 4th birthday"

n = txt.split(" ")
revWord = " ".join(reversed(n))

print(revWord)