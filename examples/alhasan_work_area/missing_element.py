"""
a function that find sthe missing element in a sequential data and 
return it

"""

def missing_element(lst):
    expected_sum_of_list = 0
    actual_sum_of_list = 0
    for i in range(lst[0], lst[-1]+1):
        expected_sum_of_list += i
    # nums is iterating through lst to get the current sum of the list
    for nums in lst:
        actual_sum_of_list += nums
    return (expected_sum_of_list - actual_sum_of_list)

print(missing_element([1, 2, 3, 5, 6]))
