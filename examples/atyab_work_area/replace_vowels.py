input_line = "hello world"
result_list = []

for character in input_line:
  if character in ["a", "e", "i", "o", "u"]:
    result_list.append("-")
  else:
    result_list.append(character)

print("".join(result_list))
