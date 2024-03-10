def count_occurrences(input_list):
    element_counts = {}

    for element in input_list:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    return element_counts


input_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = count_occurrences(input_list)
print(result)
