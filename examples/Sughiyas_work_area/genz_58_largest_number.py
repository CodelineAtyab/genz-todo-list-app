# list_numbers=[-2,0,3,2,-4,9]
# print("List of numbers= ",list_numbers)
# list_numbers.sort()
# print("Largest Numbers= ", list_numbers[-1])

list_numbers=[-2,0,3,2,-4,9]

def largest_num(list_numbers):
    largest=list_numbers[0]
    for i in list_numbers:
        if i > largest:
            largest=i
    return largest

print(largest_num(list_numbers))
