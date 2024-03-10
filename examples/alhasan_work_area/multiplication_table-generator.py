def multiplication_table():
    numbers = int(input("Enter your desired integer: "))
    for num in range(numbers):
        print(numbers, "x", num, " = ", numbers*num)
multiplication_table()