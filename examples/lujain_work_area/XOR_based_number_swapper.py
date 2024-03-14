def number_swapper(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


a = 3
b = 7
print("Numbers to swap: a =", a, ", b =", b)
a, b = number_swapper(a, b)
print("Result after swap: a =", a, ", b =", b)