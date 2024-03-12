num = [777, 5, 7, 21,559, 5, 66, 75, 2, 5, 453, 2]
largest = 0
largest2 = 0

for v in num:
    if v > largest:
        largest2 = largest
        largest = v
    elif v > largest2 and largest2 < largest:
        largest2 = v

print(largest2)

