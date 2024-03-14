"""
A program to take number of lines from the user
and output a palindrome triangle structure
"""

no_rows = int(input("Please enter the number of lines: "))

def generate_palindrom_triangle(no_rows):
    added_value = 0
    for i in range(0,no_rows+1):
        value = (10**i) + added_value
        added_value = value
        space = " " * (no_rows-i)
        print(space, (value*value))
    
generate_palindrom_triangle(no_rows)

# # Solution 2
# def generate_palindrom_triangle(no_rows):
#     string_of_ones=""
#     for i in range(1,no_rows+1):
#         string_of_ones += "1"
#         space = " " * (no_rows-i)
#         print(space, (int(string_of_ones) * int(string_of_ones)))