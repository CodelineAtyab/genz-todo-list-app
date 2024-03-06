def filter_list(num_list):
    even_result=[]
    odd_result=[]
    for num in num_list:
        if num%2==0:
            even_result.append(num)
        else:
            odd_result.append(num)
    return f"The even list is {even_result} and the odd list is {odd_result}"

input_list = [1,2,3,4,5,6,7,8]

print(filter_list(input_list))
