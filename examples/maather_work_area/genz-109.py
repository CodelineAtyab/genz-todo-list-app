'''
A function that builds a palindrome structure 
''' 
def palindrome_structure(n):
    temp = 0
    for i in range(0, n + 1):
        num = (10**i) + temp 
        temp = num
        print(f"{' ' * (n - i)}{num*num}")

palindrome_structure(7)
