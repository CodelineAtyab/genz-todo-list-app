"""
A program to check if open parantheses are
being followed by closed correct parantheses
"""

def pantheses_validation(input_list):
    parantheses_stack = []
    if len(parantheses_stack) % 2 != 0:
        return False
    for i in input_list:
        if i == "(" or i == "{" or i == "[":
            parantheses_stack.append(i)
        elif  parantheses_stack and (i == ")" and parantheses_stack[-1] == "(" or 
             (i == "}" and parantheses_stack[-1] == "{") or
             (i == "]" and parantheses_stack[-1] == "[")):
            parantheses_stack.pop()
        else:
            return False
    return True if len(parantheses_stack)==0 else False

print(pantheses_validation("[}()"))



