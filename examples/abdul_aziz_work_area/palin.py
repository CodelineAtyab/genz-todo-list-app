user_input = input("Enter a string: ")


cleaned_chars = [char.lower() for char in user_input if char.isalpha()]
cleaned_string = ''.join(cleaned_chars)


if cleaned_string == cleaned_string[::-1]:
    print("True, the string is a palindrome.")
else:
    print("False, the string is not a palindrome.")