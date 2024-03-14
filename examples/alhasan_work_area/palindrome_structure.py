"""
A function that take a desired number of rows then
it draws a palindrome structure
"""

def palindrome_structure():
    rows = int(input("Enter your desired number of rows: "))
    for i in range(1, rows+1):
        initial_value = int((10**i - 1) / 9)
        final_value = initial_value**2
        space = " " * (rows - i)
        print(space, final_value)


(palindrome_structure())


# Another solution
# def palindrome_structure():
#     rows = int(input("Enter your desired number of rows: "))
#     x = ""
#     for i in range(1, rows+1):
#         x = x + "1"
#         formatting = " " * (rows - i)
#         final = int(x) * int(x)
#         print(formatting, final)

# palindrome_structure()