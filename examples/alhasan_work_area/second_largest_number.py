'''
A function which takes a list as an input then return
the second largest element in that list

'''


def second_largest(nums_list):
    largest_number = nums_list[0]
    second_largest_number = float("-inf")

    for number in nums_list:
        if number > largest_number:
            second_largest_number = largest_number
            largest_number = number
        elif number > second_largest_number and number != largest_number:
            second_largest_number = number
    return(second_largest_number)



user_input = input("Enter your desired list of numbers with a space between them: ")
nums_list = [int(x) for x in user_input.split()]
print(second_largest(nums_list))

