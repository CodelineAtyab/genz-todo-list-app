def palindrome_var(s):
    modified_s = s.replace(" ","")
    j = len(modified_s) - 1
    for i in range(len(modified_s)//2):
        if modified_s[i].lower() != modified_s[j].lower():
            return False
        j -= 1
    return True
