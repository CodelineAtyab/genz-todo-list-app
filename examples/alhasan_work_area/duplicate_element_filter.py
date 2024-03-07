def remove_duplicate_filter(lst):
    modified_list = []
    for nums in lst:
        if nums not in modified_list:
            modified_list.append(nums)
    return modified_list

print(remove_duplicate_filter(["ali", "ali", "alhasan"]))
print(remove_duplicate_filter([1, 1, 3, 4, 5]))

