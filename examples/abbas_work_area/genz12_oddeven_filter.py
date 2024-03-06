user_input = input("Enter multiple integers separated by spaces: ")
evenlist = []
oddlist = []
list = [int(x) for x in user_input.split()]
parity = input("Enter Even or Odd: ")

for x in list:
    if x % 2 == 0 and parity == "Even":
        evenlist.append(x)
    elif x % 2 != 0 and parity == "Odd":
        oddlist.append(x)
if parity == "Even":
    print(evenlist)
else:
    print(oddlist)