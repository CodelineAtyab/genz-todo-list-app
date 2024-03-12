"""
a tool that verifies if perenthesis are properly closed or not

"""

def perenthesis(user_input):
    stack = []
    result = ""
    for char in user_input:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


print(perenthesis("))(("))
print(perenthesis("()"))
print(perenthesis(")"))