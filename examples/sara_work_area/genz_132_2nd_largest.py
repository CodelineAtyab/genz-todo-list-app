"""
A program to find the second
largest number from a list
"""

def second_largest_num_finder(input_list):
    largest, second_largest = float("-inf"), float("-inf")
    for i in input_list:
        if i>largest:
            second_largest = largest
            largest = i
        elif i>second_largest:
            second_largest = i
    return second_largest

print(second_largest_num_finder([1, 7, 3, 9, 3, -2]))


# # Solution 2
# def second_largest_num_finder(input_list):
#     input_list.sort()
#     return input_list[-2]

# print(second_largest_num_finder([1, 7, 3, 9, 3, -2]))