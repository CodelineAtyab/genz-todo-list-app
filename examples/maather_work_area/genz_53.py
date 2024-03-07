def missing_element(lst):
    complete_lst = list(range(1,len(lst)+2))
    missing = sum(complete_lst) - sum(lst)
    return missing

# example
lst = [1,2,3,5,6]
print(missing_element(lst))