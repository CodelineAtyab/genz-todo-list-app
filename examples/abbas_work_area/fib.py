user = input("Enter stuff: ")
lists = [x for x in user.split()]

frequency = dict()

for x in lists:
    if x not in frequency:
        frequency[x] = 1
    else: 
        frequency[x] += 1

print(frequency)