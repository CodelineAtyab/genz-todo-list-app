def palindrome_verification_tool(str_input):
    str1 = "".join(str_input.split())
    str2 = str1[::-1]
    if str1.lower() == str2.lower():
        return True
    else:
        return False

str_input = "A man a plan a canal Panama"
print(palindrome_verification_tool(str_input))