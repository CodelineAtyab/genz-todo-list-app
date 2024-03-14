user_input = int(input("Enter: "))

def palindrome(user_input):
    f = " "
    for i in range(1, user_input+1):
        f = f + "1" 
        space = user_input - i
        triangle = " " * space
        print(triangle, int(f) * (int(f)))

palindrome(user_input)