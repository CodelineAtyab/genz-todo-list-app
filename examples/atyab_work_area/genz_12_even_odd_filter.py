def filter_even_numbers(list_of_num):
  result_list = []
  for curr_num in list_of_num:
    if curr_num % 2 == 0:
      result_list.append(curr_num)
  return result_list

def filter_odd_numbers(list_of_num):
  result_list = []
  for curr_num in list_of_num:
    if curr_num % 2 == 1:
      result_list.append(curr_num)
  return result_list

list_of_all_nums = [1, 2, 3, 4, 5, 6, 7, 8]

print(filter_even_numbers(list_of_all_nums))
print(filter_odd_numbers(list_of_all_nums))
