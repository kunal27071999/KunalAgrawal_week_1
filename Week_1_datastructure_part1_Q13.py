"""13. Using Ternary operator or COnditional operator: Identify maximum of three numbers """

a = 10
b = 20
c = 3

print(a if (a > b and a > c) else (b if (b > a and b > c)else c))
