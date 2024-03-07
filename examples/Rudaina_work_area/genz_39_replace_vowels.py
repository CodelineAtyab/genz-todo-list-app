

input_str = "hello world"
temp = []
def replec_vowels(input_str):
    
    for i in input_str:
        if i in ["a", "e", "i", "o", "u"]:
            temp.append("-")
        else:
            temp.append(i)
    return ("".join(temp))

print(replec_vowels(input_str))