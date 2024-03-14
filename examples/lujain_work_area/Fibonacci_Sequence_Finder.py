def fibonacci_seq_generator(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fs = [0, 1]
        while len(fs) < n:
            next_number = fs[-1] + fs[-2]
            fs.append(next_number)
        return fs[:n]
input = 8
fibonacci_seq = fibonacci_seq_generator(input)
print(fibonacci_seq)