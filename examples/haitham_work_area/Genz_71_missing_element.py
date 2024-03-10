def find_missing_number(total_list):
    n = len(total_list) + 1
    total_sum = n * (n + 1) // 2
    list_sum = sum(total_list)
    missing_number = total_sum - list_sum
    return missing_number

my_list = [1,2,3,5,6]
missing_number = find_missing_number(my_list)
print('The missing number is: ', missing_number)