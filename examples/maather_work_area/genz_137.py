'''
A function that swaps two numbers using the XOR bitwise operation.
It takes two numbers as input and ensures that the original values are 
successfully exchanged without any data loss.
'''

def xor_swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"a = {a}, b = {b}")

xor_swap(3,4)