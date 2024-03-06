def even_numbers(list_of_num):
    results = []
    for even1 in list_of_num:
        if even1 % 2 == 0:
            results.append(even1)
    return results

def odd_numbers(list_of_num):
    results = []
    for odd1 in list_of_num:
        if odd1 % 2 == 1:
            results.append(odd1)
    return results

randoms = [1,2,3,4,5,6,7,8,9,10]

print('Even:',even_numbers(randoms))
print('Odd: ',odd_numbers(randoms))

