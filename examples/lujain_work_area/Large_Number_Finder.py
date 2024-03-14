def largest_number_finder(numbers):
    if not numbers:
        return None
    
    return max(numbers)


input = [-2, -3, 4, 5, -7, 6]
largest_number = largest_number_finder(input)
print("Largest number:", largest_number)