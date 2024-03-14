n = int(input('Enter the size of the palindrome structure: '))

for i in range(1, n + 1):
    print(' '*(n-i), end='')
    print(''.join(str(j) for j in range(1, i)), end='')
    print(''.join(str(j) for j in range(i, 0, -1)))