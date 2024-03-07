lst = input("Enter a list of numbers separated by spaces: ")
lst = [int(x) for x in lst.split()]  
unique_numbers = set(lst)  
lst = list(unique_numbers)  
print(lst)