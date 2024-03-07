input_list = [1, 2, 3, 4, 5, 7]

def missing_element_finder(input_list):
    for element in range(input_list[0], input_list[-1]+1):
        if element not in input_list:
            return element

print(missing_element_finder(input_list))