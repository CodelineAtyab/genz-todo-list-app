def frequency_counter(input_list):
    result = {}
    for item in input_list:
        if item not in result:
            result[item] = input_list.count(item)
    return result  

print(frequency_counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))