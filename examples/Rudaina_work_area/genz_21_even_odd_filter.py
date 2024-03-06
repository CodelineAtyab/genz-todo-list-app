num_list = [1, 2, 3, 4, 5, 6, 7, 8]

def even_num_filter(num_list):
    temp_even = []
    temp_odd = []
    for i in num_list:
        if i % 2 == 0:
            temp_even.append(i)
        else:
            temp_odd.append(i)
    return f'Even numbers are {temp_even} and Odd numbers are {temp_odd}'
    
print(even_num_filter(num_list))