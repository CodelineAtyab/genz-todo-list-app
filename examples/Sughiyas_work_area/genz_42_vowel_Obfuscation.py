input_sentence= "Hello World"
result_list=[]


for character_found in input_sentence:
    if character_found in ["a","e","i","o","u"]:
        result_list.append("-")
    else:
        result_list.append(character_found)


print("".join(result_list))