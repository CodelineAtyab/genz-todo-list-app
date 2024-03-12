a = input("Enter a string to check if palindrome: ")
a1="".join(a.split())
a2=a1[::-1]

if a2.lower()==a1.lower():
    print("True")
else:
    print("False") 