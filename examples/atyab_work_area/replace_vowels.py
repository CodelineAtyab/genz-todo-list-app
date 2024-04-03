def replace_vowels_with(word, symbol="-"):
    validated_word = "" if word is None else word
    result_list = []
    for character in validated_word:
        if symbol and character in ["a", "e", "i", "o", "u"]:
            result_list.append(symbol)
        else:
            result_list.append(character)

    return "".join(result_list)


if __name__ == "__main__":
  print(replace_vowels_with("Hello World", "@"))