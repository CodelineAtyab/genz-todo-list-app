"""
a tool that verifies if perenthesis are properly closed or not

"""


def perenthesis(user_input):
    brackets_start = "("
    bracket_end = ")"
    check = []
    check2 = []

    for i in user_input:
        if i == brackets_start:
            check.append(i)
        elif i == bracket_end:
            check2.append(i)
        
    if len(check) == len(check2):
        print("True")
    else:
        print("False")

perenthesis("(())")