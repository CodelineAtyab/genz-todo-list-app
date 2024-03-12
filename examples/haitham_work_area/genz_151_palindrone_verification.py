def palindrome_verification(sentence):
    s1 = ''.join(sentence.split())
    s2 = s1[::-1]
    if s1.lower() == s2.lower():
        return True
    else:
        return False
sentence = "A man a plan a canal Panama"
print(palindrome_verification(sentence))
