def largest_number(lst):
    rslt = lst[0]
    for i in lst:
        if i > rslt:
            rslt = i
    return rslt

lst = [-1, 3, 5, 7, 9, 2]
print(largest_number(lst))

