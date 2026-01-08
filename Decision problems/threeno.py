a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is largest")
elif b > c:
    print(b, "is largest")
else:
    print(c, "is largest")

"""
output
Enter first number: 12
Enter second number: 34
Enter third number: 45
45 is largest
"""