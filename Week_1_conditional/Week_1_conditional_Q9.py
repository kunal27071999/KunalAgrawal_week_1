"""9. WAP to print the season, print Summer,if month entered is between March to June, print Monsoon
 if month entered is between July to October and Winter if if month entered is between November to Feb."""

month = "October"
if month in ("March", "April", "may", "june"):
    print("Summer")
elif month in ("july", "august", "september", "October"):
    print("Monsoon")
else:
    print("Winter")
