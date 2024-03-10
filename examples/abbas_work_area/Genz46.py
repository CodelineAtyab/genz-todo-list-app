#user = input("Enter a list of number: ")
num = [1, 2, 1]
largest = num[0]
for v in num:
    if v > largest:
        largest = v
print(largest)