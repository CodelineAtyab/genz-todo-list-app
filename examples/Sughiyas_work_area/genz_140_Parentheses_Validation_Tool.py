def val_paren(str_paren):
    stack_paren = []
    open_paren = '('
    close_paren = ')'

    for char in str_paren:
        if char == open_paren:
            stack_paren.append(char)
        elif char == close_paren:
            if not stack_paren:
                return False  # no matching paren
            stack_paren.pop()

    return len(stack_paren) == 0 #true if all paren are matched
    
print(val_paren("((()()))"))
print(val_paren("((())"))     
print(val_paren("()()()"))   
print(val_paren("())("))      
print(val_paren(""))