
def check_brackets(input):
    stack = []
    
    for i in range(len(input)):

        if input[i] == "(":
            stack.append(input[i])
        elif input[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        
        if i == len(input)-1 and len(stack) != 0:
            return False
        elif i == len(input)-1 and len(stack) == 0:
            return True

print(check_brackets("(())"))
print(check_brackets("))"))
print(check_brackets("(("))
print(check_brackets("))(("))