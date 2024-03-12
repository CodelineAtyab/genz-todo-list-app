a = int(input("Enter first num: "))
b = int(input("Enter second num: "))

a = a ^ b
b = a ^ b
a = a ^ b

print(f"first number is now {a} and second number is now {b}")
