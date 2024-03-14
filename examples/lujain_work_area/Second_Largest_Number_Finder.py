def second_largest_number_finder(numbers):
    sorted_numbers = sorted(set(numbers), reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None


input = [4, 3, 5, 8, 1, 6]
print("Second largest number:", second_largest_number_finder(input))