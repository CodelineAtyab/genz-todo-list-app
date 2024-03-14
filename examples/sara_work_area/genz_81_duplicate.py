def duplicate_filter(input_list):
    result_set = []
    for item in input_list:
        if item not in result_set:
            result_set.append(item)
    return result_set

print(duplicate_filter([1, 1, 2, 3, 4, 4, 5]))
print(duplicate_filter(['Cat', 'Dog', 'Cat', 'Mouse']))