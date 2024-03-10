def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

# Example usage:
input_number = 5
result = generate_fibonacci(input_number)
print(result)