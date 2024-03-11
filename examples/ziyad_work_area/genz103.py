input = input("Enter: ")

input = input.replace(" ", "")
input = input.replace(",", "")
input = input.replace(".", "")
input = input.replace(":", "")
input = input.replace(";", "").lower()

input_reverse = input[::-1]
if input == input_reverse:
    print(True)
else:
    print(False)