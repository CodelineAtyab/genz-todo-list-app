def missing_element(lst):
    temp = list(range(1,(len(lst)+2)))
    missing_elem = (sum(temp) - sum(lst))
    return missing_elem

print(missing_element([1, 2, 4, 5, 6, 7]))