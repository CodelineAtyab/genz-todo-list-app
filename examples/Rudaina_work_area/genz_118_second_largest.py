
'''
    The second largest number finder function except a list of numbers 
    as an input and it will return the the secod largest number in the list 

'''
def second_largest_number_finder(lst):
    largest_num = lst[0]
    second_largest = largest_num
    for i in lst:
        if i > second_largest:
            if i > largest_num:
                second_largest = largest_num
                largest_num = i
            else:
                second_largest = i
    return second_largest

lst = [5, 1, 9, 7, 2, 6]
print(second_largest_number_finder(lst))