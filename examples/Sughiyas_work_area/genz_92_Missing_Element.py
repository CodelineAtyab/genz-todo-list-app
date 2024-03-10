def missing_ele(list_num):

    n = len(list_num) + 1
    expc_sum = sum(range(1, n + 1))
    act_sum = sum(list_num)

    missing_ele = expc_sum - act_sum
    return missing_ele

list_num= [1, 2, 3, 5]
res = missing_ele(list_num)
print(res, " is missing")
