'''
the xor_swap_elem function excepts 2 integers as 'a' and 'b' 
the function will swap the 2 integers using the xor operation  
it will return the swapped numbers 
'''
def xor_swap_elem(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(f'a: {a} and b: {b}')

xor_swap_elem(4 , 3)
