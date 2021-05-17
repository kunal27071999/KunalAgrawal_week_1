"""13. WAP to print Student is passed if student scores more than 40 marks in Physics ,Chemistry and Maths"""

physics = 40
chemistry = 50
maths = 200

if physics > 40 :
    if chemistry and maths > 40:
        print("Student is passed")
    else:
        print("Student is fail")
else:
    print("Student is fail")
