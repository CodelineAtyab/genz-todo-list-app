user = input("Enter: ").strip().replace(" ", "").lower()
punc = []

for curr in user:
    if curr not in [",", "-", "."]:
        punc.append(curr)

remove = "".join(punc)

punc1 = punc[::-1]

if punc == punc1:
    print("True")
else:
    print("False")