num = int(input("Enter: "))
a = 0
b = 1
c = a + b
f = [0, 1]
for i in range(num-2):
    f.append(c)
    a = b
    b = c
    c = a + b
print(f)