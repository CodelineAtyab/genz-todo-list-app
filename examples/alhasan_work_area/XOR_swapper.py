"""
A function that takes two integers and swap their values using xor operator ^
"""

def xor_swapper():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    x = x ^ y
    y = x ^ y
    x = x ^ y

    print("Your swapped numbers are: ", "first number =", x, " && ", "second number =", y)

xor_swapper()