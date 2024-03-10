def largest(lst):
    max = lst[0]
    for number in lst[1:]:
        if number > max:
            max = number
    return max