p = float(input("Enter percentage: "))
if p >= 90:
    print("O (Outstanding)")
elif p >= 85:
    print("A+ (Excellent)")
elif p >= 80:
    print("A (Very Good)")
elif p >= 70:
    print("B+ (Good)")
elif p >= 60:
    print("B (Above Average)")
elif p >= 50:
    print("C (Average)")
elif p >= 45:
    print("P (Pass)")
else:
    print("F (Fail)")


"""
output
Enter percentage: 90
O (Outstanding)
"""