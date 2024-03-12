def missing_elements_finder(sequence):
    n = len(sequence)
    expected_sum = (n + 1) * (sequence[0] + sequence[-1]) // 2
    actual_sum = sum(sequence)
    missing_elements = []
    for i in range(sequence[0], sequence[-1] + 1):
        if i not in sequence:
            missing_elements.append(i)
    return missing_elements

input = [1, 2, 5, 7, 9, 11, 13, 14]
missing_numbers = missing_elements_finder(input)
print(missing_numbers)