
def Multiplication_table_generator(n):
    for i in range(1,11):
        x = n * i
        print(f'{n} * {i} = {x}')


n = int(input("Enter a number: "))
Multiplication_table_generator(n)