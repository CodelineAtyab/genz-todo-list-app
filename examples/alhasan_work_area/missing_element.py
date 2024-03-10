def missing_element(lst):
    expected_sum_of_list = 0
    actual_sum_of_list = 0
    for i in range(lst[0],lst[-1]+1):
        expected_sum_of_list = expected_sum_of_list + i
    for n in lst:
        actual_sum_of_list += n
    return (expected_sum_of_list - actual_sum_of_list)

print(missing_element([1,2,3,5,6]))
