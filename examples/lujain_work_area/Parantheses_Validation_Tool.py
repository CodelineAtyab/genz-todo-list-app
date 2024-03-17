def parentheses_validation_tool(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

#for when output is True
print(parentheses_validation_tool("((()()))")) 
#for when output is False
print(parentheses_validation_tool("(()"))