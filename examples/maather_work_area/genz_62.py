ex = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

def element_count(lst):
    dict = {}
    for i in lst:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(element_count(ex))