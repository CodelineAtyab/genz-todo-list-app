def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest

input_list = [5, 1, 9, 7, 2, 6]
second_largest = find_second_largest(input_list)
print("Second largest number:", second_largest)
