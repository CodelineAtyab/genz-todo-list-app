'''
The function parentheses_validation_tool accept a string containing any number of parentheses.
The function use stack to validate, if its an open paranthesis it will be added to the stack
if its a closed paranthesis from the string it will pop one from the stack if it is valid 
it will return false if its not valid and true when the stack is empty 
'''
def parentheses_validation_tool(input_str):
    stack = []
    validation = { ')' : '(' }
    for char in input_str:
        if char in validation:
            if stack:
                elem = stack.pop()
            else:
                elem = '!'
            if validation[char] != elem:
                return False
        else:
            stack.append(char)
    return not stack

print(parentheses_validation_tool("((()))"))
print(parentheses_validation_tool("(()()))"))
print(parentheses_validation_tool("()))"))