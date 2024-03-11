'''
A function that builds a triangle palindrome structure 
ex : palindrome_structure(5)
       1
      121
     12321
    1234321
   123454321
''' 
def palindrome_structure(n):
    temp = 0 #stores the value of the previous num , starting with 0
    for i in range(0, n + 1):
        num = (10**i) + temp 
        temp = num
        print(f"{' ' * (n - i)}{num*num}")

palindrome_structure(7)
