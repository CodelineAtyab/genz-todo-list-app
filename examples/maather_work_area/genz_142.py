'''
A function that validates the correct pairing and nesting of opening and closing parentheses in a string.
Example:
Input string = "((()))"
Output = True
'''
def parentheses_validation(str):
    stack = [] 
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for bracket in str:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False

    return True


print(parentheses_validation("(({}))"))
print(parentheses_validation("({}])"))