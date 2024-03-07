def replace_vowels(word):
    vowels_list = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in word:
        if char in vowels_list: 
            word = word.replace(char, "-")
    return word

print(replace_vowels('Hello GenZ!'))

