vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

input_string = input()
result = []

for character in input_string:
    if character in vowels:
        result.append("-")
    else:
        result.append(character)

print("".join(result))