import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
p = a + b + c
s = p / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Perimeter =", p)
print("Area =", area)

"""
Enter side a: 2
Enter side b: 3
Enter side c: 4
Perimeter = 9.0
Area = 2.9047375096555625
"""