string_input = input("Enter a string to check if palindrome: ")
string1 = "".join(string_input.split()) #removing white spaces in the input string
string2 = string1[::-1]

if string2.lower()==string1.lower(): 
    print("True")
else:
    print("False") 
