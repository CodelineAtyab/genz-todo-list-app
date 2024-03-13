stack = []

input_string = input("Enter a string with parentheses: ")

for char in input_string:
    if char == '(':
        stack.append(char)
    elif char == ')' and stack:
        stack.pop()

result = not stack
print(result)