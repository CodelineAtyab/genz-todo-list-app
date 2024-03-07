input_string = "Hello World"
result_string = []

for character in input_string:
    if character in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        result_string.append("-")
    else:
        result_string.append(character)

print("".join(result_string))