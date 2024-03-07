user = input("Enter a list of number: ")
num = [int(x) for x in user.split()]
print(max(num))