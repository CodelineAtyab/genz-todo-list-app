def parentheses_validation(string1):
    stack = []

    for char in string1:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack
print(parentheses_validation('(((())))'))
print(parentheses_validation('(((())'))
print(parentheses_validation('()()()'))