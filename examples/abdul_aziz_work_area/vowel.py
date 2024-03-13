input_string = "Hello World"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
output_string = ''.join(['-' if char in vowels else char for char in input_string])

print(output_string)