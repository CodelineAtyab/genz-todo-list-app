def replace_vowel(vowel):
    vowel_list = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for x in vowel_list:
        vowel = vowel.replace(x,"-" )
    return vowel
    
print(replace_vowel("Hello World"))