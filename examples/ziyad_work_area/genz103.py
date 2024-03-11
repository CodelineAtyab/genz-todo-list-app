input = input("Enter: ")

input = input.replace(" ", "")
input = input.replace(",", "")
input = input.replace(".", "")
input = input.replace(":", "")
input = input.replace(";", "").lower()

is_palindrome = True
start_index = 0
end_index = len(input) - 1

for i in range(int(end_index / 2)):
    if not input[start_index] == input[end_index]:
        is_palindrome = False
    start_index += 1
    end_index -= 1

print(is_palindrome)