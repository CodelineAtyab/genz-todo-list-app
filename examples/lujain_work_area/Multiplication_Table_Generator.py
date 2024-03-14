def multiplication_table_generator(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        

n = 3
print(f"Multiplication table for number {n}:")
multiplication_table_generator(n)