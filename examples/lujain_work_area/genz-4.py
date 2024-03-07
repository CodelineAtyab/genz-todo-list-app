n = "The quick brown fox jumped over the lazy dog"
l = []

for character in n:
  if character in ["a", "e", "i", "o", "u"]:
    l.append("-")
  else:
    l.append(character)

print("".join(l))