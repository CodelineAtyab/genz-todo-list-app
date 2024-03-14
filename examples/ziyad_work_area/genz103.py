input = input("Enter to check if palindrome: ")

# Remove spaces and punctuation, and convert to lowercase letters
input = input.replace(" ", "")
input = input.replace(",", "")
input = input.replace(".", "")
input = input.replace(":", "")
input = input.replace(";", "").lower()

# Reverse string and check equality
input_reverse = input[::-1]
if input == input_reverse:
    print(True)
else:
    print(False)