n = int(input("Enter a two-digit number: "))

a = n // 10
b = n % 10

if a > b:
    print("larger number is:",a)
else:
    print("larger number is:",b)

"""
output
Enter a two-digit number: 23
larger number is: 3
"""