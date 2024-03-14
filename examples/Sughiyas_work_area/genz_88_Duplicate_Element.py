def rem_dup(list_num):
    non_dup_list = []
    dub_list = []

    for x in list_num:
        if x not in dub_list:
            non_dup_list.append(x)
            dub_list.append(x)

    return non_dup_list

list_num = [1, 2, 2, 3, 3, 4, 5, 5]
res = rem_dup(list_num)
print(res)
