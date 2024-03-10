def palindrome_verification(input_str):
    new_input_string = "".join(input_str.split())
    reversed_string = new_input_string[::-1]
    if new_input_string.lower() == reversed_string.lower():
        return "True, the string is a palindrome"
    else:
        return "False, the string is not a palindrome"

print(palindrome_verification("sara aras"))