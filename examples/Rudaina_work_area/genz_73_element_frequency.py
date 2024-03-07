def element_frequency_counter(input_lst):
    rslt_dict = {}
    for i in input_lst:
        if i in rslt_dict:
            rslt_dict[i] += 1
        else:
            rslt_dict[i] = 1
    return rslt_dict

input_lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(element_frequency_counter(input_lst))