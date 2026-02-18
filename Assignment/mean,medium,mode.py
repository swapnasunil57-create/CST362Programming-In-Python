numbers = input("Enter numbers separated by space: ")
num_list = numbers.split()

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

""" MEAN"""
total = 0
for num in num_list:
    total = total + num

mean = total / len(num_list)

""" MEDIAN"""
num_list.sort()
n = len(num_list)

if n % 2 == 0:
    median = (num_list[n//2 - 1] + num_list[n//2]) / 2
else:
    median = num_list[n//2]

""" MODE"""
count = {}

for num in num_list:
    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1

mode = max(count, key=count.get)


print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)


""""output"""
Enter numbers separated by space: 1 2  2  3 4
Mean: 2.4
Median: 2
Mode: 2