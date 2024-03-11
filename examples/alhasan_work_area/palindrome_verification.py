def palindrome_verification(word):
    new_word = word.replace(" ", "").replace(",", "").lower()
    reversed_word = new_word[::-1]
    if reversed_word == new_word:
        return True
    else:
        return False
print(palindrome_verification("A man a plan a canal, Panama"))
print(palindrome_verification("alhasan"))