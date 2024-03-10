user = input("Enter: ")
num = [int(x) for x in user.split()]

n = num[-1] + 1
n2_val = num[1] - 1
for i in range(n2_val, n):
    if i not in num:
        print(i)

