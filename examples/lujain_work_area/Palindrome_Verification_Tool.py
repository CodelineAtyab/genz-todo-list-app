def palindrome_verification_tool(str):
    str = ''.join(char.lower() for char in str if char.isalnum())
    return str == str[::-1]


input = "LeVeL"
print(palindrome_verification_tool(input))