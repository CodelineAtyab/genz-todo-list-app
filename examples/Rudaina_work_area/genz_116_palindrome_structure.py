
def palindrome_structure(n):
    x = ""
    for i in range(1,n+1):
        x = x + "1"
        # z = x.replace("1", " ")
        z = " " * (n-i)
        print(f'{z} {int(x) * int(x)}')
        
palindrome_structure(4)