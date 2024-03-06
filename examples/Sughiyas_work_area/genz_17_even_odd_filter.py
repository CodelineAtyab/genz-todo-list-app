def filtered_numbers(list_numbers):
    odd_num=[]
    even_num=[]

    for curr_num in list_total_numbers:
        if curr_num % 2 ==0:
            even_num.append(curr_num)
        else:
            odd_num.append(curr_num)
    return "Even Numbers= " +str(even_num) + " and Odd numbers= " +str(odd_num)

list_total_numbers=[3,5,2,4,8,9,0,7]
print(filtered_numbers(list_total_numbers))