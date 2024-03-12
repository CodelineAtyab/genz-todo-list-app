a = input("Enter a string to check if palindrome: ")
b = a[::-1]

if b==a[::-1]:
    print("True")
else:
    print("False")    