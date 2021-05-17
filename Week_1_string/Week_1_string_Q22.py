"""22. Formatting the string 
name = "Chistats"
year = "2017"
age = "4"
Use below formats to print the statement as "Chistats is established in the 2017 and today we are celebrating 4th birthday"
	1. {} {} {}
	2. {0} {1} {2}
	3. {name} {year} {age} """

txt = "{name} is established in the {year} and today we are celebrating {age} birthday".format(name = "Chistats",year = "2017", age = "4")
print(txt)

txt1 = "{0} is established in the {1} and today we are celebrating {2} birthday".format("Chistats", "2017", "4")
print(txt1)
