user_input = input("Enter: ").strip().replace(" ", "").lower()
punctuation = []

for curr in user_input:
    if curr not in [",", "-", "."]:
        punctuation.append(curr)

remove = "".join(punctuation)

inverse = punctuation[::-1]

if punctuation == inverse:
    print("True")
else:
    print("False")