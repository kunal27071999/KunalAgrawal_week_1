"""24. WAP to print the reverse interna content of each word from statement "Chistats is established in the 2017 and today we are celebrating 4th birthday"""

txt = "Chistats is established in the 2017 and today we are celebrating 4th birthday";

temp = txt.split(" ")


revtxt = [i[::-1] for i in temp]

revsentence = " ".join(revtxt)
print(revsentence)
