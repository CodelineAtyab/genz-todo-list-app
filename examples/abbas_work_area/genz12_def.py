def even_filter(list_of_num):
    result = []
    for x in list_of_num:
        if x % 2 == 0:
            result.append(x)
    return result
    
random = [1, 2, 3, 4, 5, 6]
print(even_filter(random))

def odd_filter(list_of_num):
    result = []
    for x in list_of_num:
        if x % 2 != 0:
            result.append(x)
    return result
 
print(odd_filter(random))

