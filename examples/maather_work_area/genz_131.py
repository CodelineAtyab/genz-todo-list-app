'''
This function takes a list of numbers and retuns the second largest number.
It handles litst with all unique elements.
lst: a list of numbers.
'''

def second_largest(lst):
    if len(lst) < 2:
        return "Error: List should have at least two elements"
    
    largest = float('-inf')
    second_largest = float('-inf')

    for n in lst:
        if n > largest:
            second_largest = largest
            largest = n
        elif n > second_largest:
            second_largest = n

    return second_largest

# lst = [5, 1, 9, 7, 2, 6]
lst = [1, 2, 3]
print(second_largest(lst))
