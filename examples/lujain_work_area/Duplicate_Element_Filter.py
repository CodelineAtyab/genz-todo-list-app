def duplicate_element_filter(input):
    unique_list = []
    for element in input:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input = [6, 3, 1, 3, 8, 1, 5, 9]
result = duplicate_element_filter(input)
print(result)