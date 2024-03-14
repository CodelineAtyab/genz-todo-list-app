def palindrome_triangle_generator(n):
    for i in range(1, n + 1):
        row = ' '.join(str(j) for j in range(1, i + 1))
        print(row.center(n * 2 - 1))


input = 5
palindrome_triangle_generator(input)