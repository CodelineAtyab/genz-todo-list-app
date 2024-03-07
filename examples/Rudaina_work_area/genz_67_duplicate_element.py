def duplicate_element(lst):
    rslt = []
    for i in lst:
        if i not in rslt:
            rslt.append(i)
    return rslt
    
print(duplicate_element([1, 2, 2, 3, 4, 4, 5]))
