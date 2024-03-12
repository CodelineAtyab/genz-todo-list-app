def frequency_finder(list_of_elements):
    element_frequency = {}
    for e in list_of_elements:
        if e in element_frequency:
            element_frequency[e] += 1
        else:
            element_frequency[e] = 1
    return element_frequency

input = ['blue', 'red', 'yellow', 'red', 'blue','blue','green']
result = frequency_finder(input)
print(result)