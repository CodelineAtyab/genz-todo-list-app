'''

A function which validate the correct pairing and nesting of 
opening and closing parentheses in a string using a stack

'''


def isValid(parentheses):
    stack = []
    pairs_of_parentheses = {")":"("}
    for pair in parentheses:
        if pair in pairs_of_parentheses.values():
            stack.append(pair)
        elif pair in pairs_of_parentheses.keys():
            if len(stack) == 0 or stack.pop() != pairs_of_parentheses[pair]:
                return False
    return len(stack) == 0


print(isValid("))"))
print(isValid("(())"))
print(isValid("()))()"))

