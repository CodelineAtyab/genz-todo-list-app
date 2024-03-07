input_line = "Hello World"

for char in input_line:
    if char in ["A","E", "I", "O", "U" "a", "e", "i", "o", "u"]:
       input_lines = input_line.replace(char, "-")
print(input_lines)