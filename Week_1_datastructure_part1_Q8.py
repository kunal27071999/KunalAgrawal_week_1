"""8. Using logical operators: WAPTP "Student is failed" if he scores 40- marks in atleast one subject from Physics and Maths"""

physics = 4
maths = 40

if (physics and maths) > 40:
    print("Pass")
else:
    print("Fail")
