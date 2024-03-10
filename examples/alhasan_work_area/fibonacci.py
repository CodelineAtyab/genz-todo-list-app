def fibonacci(series):
    a = 0
    b = 1
    if series == 0:
        return []
    elif series == 1:
        return [0]
    else:
        result = [0,1]
        for i in range(series):
            c = a + b
            result.append(c)
            a = b
            b = c    
        return result

print(fibonacci(10))   


def missing_element(lst):
    expected_sum_of_list = 0
    actual_sum_of_list = 0
    for i in range(lst[0],lst[-1]+1):
        expected_sum_of_list = expected_sum_of_list + i
    for n in lst:
        actual_sum_of_list += n
    return (expected_sum_of_list - actual_sum_of_list)

print(missing_element([1,2,3,5,6]))
