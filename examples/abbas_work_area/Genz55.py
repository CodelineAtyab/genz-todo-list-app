user = input("Enter a list of number: ")
num = [int(x) for x in user.split()]
num = set(num)
print(num)