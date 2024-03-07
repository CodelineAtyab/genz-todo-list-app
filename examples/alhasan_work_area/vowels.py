def replace_vowels(word):
    vowels_list = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in word:
        if char in vowels_list: 
            replaced_word = word.replace(char, "-")
        else:
            replaced_word = word
    return replaced_word

print(replace_vowels('eee'))

