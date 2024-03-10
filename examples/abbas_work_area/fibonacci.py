num = int(input("Enter: "))
a = 0
b = 1
c = a + b
print(a)
print(b)
for i in range(num-2):
    print(c)
    a = b
    b = c
    c = a + b
