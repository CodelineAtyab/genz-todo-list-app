input = [5, 1, 9, 7, 2, 8, 5, 11, 14, 33, 38, 6]

largest = -999999
second_largest = -999999

for i in input:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and largest > second_largest:
        second_largest = i


print(second_largest)
