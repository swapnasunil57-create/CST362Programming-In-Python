a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b*b - 4*a*c
if d > 0:
    print("Two real and distinct roots")
elif d == 0:
    print("Two real and equal roots")
else:
    print("Imaginary roots")

"""
output
Enter a: 3
Enter b: 2
Enter c: 4
Imaginary roots
"""