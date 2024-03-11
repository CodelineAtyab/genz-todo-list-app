'''
This function prints the multiplication table of a given number (n) up to 10
'''
def multiplication_table_generator(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


multiplication_table_generator(5)