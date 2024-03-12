"""
A function to 
"""

def palindrome_structure():
    rows = int(input("Enter your desired number of rows: "))
    for i in range(1, rows+1):
        initial_value = int((10**i-1) / 9)
        final_value = initial_value**2
        formating = " " * ((i-1)+1)
        print(formating, final_value, formating)
    
(palindrome_structure())