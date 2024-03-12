input = [5, 1, 9, 7, 2, 8, 5, 11, 14, 33, 38, 6]

largest = input[0]
second_largest = input[0]

for i in input:
    if i > largest:
        second_largest = largest
        largest = i

print(second_largest)
