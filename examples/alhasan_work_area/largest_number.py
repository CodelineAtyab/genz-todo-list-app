# def find_largest_number(nums):
#     return max(nums)
# print(find_largest_number([1, 89, 1010, 50, 90]))

def find_largest_number(nums):
    largest_number = nums[0]
    for number in nums:
        if number > largest_number:
            largest_number = number
    return largest_number

print(find_largest_number([94, 1, 2, 3, 4, 50, 500, 150]))

