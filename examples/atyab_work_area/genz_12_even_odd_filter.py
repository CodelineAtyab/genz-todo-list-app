def filter_even_odd_numbers(list_of_nums):
  even_numbers = []
  odd_numbers = []

  for curr_num in list_of_all_nums:
    if curr_num % 2 == 0:
      even_numbers.append(curr_num)
    else:
      odd_numbers.append(curr_num)
  
  return f"Even numbers are {even_numbers} and Odd numbers are {odd_numbers}"

list_of_all_nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(filter_even_odd_numbers(list_of_all_nums))
