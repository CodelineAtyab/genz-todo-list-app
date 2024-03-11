'''
A function that validates the correct pairing and nesting of opening and closing parentheses in a string.
Example:
Input string = "((()))"
Output = True
'''
def parentheses_validation(str):
    dict = {}
    dict['open'] = str.count('(')
    dict['close'] = str.count(')')

    if dict['open'] == dict['close']:
        return True
    return False
