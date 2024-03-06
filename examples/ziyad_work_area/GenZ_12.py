
def filter_even(list_of_nums):
    result_list = []
    for num in list_of_nums:
        if num % 2 == 0:
            result_list.append(num)
    return result_list

def filter_odd(list_of_nums):
    result_list = []
    for num in list_of_nums:
        if num % 2 != 0:
            result_list.append(num)
    return result_list


print(filter_even([1, 2, 3, 4, 5, 6]))
print(filter_odd([1, 2, 3, 4, 5, 6]))