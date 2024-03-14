n = int(input('Enter a num: '))
a, b = 0, 1
fib_seq = []

while a < n:
    fib_seq.append(a)
    a, b = b, a + b 

print(', '.join(map(str, fib_seq)))