"""
A function to check if a given string is a palindrome and returns a
boolean value indicating whether or not the string is a palindrome.

"""
def palindrome_verification(word):
    new_word = word.replace(" ", "").replace(",", "").lower()
    reversed_word = new_word[::-1]
    if reversed_word == new_word:
        return True
    else:
        return False
print(palindrome_verification("A man a plan a canal, Panama"))
print(palindrome_verification("alhasan"))
