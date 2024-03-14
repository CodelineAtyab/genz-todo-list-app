list = [-1, 3, 5, 7, 9, 2]

largest = list[0]

for num in list:
    if num > largest:
        largest = num

print(largest)