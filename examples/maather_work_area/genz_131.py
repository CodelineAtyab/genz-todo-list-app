'''
This function takes a list of numbers and retuns the second largest number.
It handles litst with all unique elements.
lst: a list of numbers.
'''
def second_largest(lst):
    largest = 0
    second_largest = 0
    
    for n in lst:
        if n > largest and n > second_largest:
            largest = n
        elif n > second_largest and n < largest :
            second_largest = n
    
    return second_largest

lst = [5, 1, 9, 7, 2, 6]
print(second_largest(lst))