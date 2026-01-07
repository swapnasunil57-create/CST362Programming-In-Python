sec = int(input("Enter seconds: "))
h = sec // 3600
m = (sec % 3600) // 60
s = sec % 60
print("Hours:", h)
print("Minutes:", m)
print("Seconds:", s)

"""
output:
Enter seconds: 30
Hours: 0
Minutes: 0
Seconds: 30
"""