#Another approach

# evenList = []
# oddlist = []
# user_input_list = input("Enter your desired list of numbers with a space between them: ")
# input_list = [int(x) for x in user_input_list.split()]
# user_input = input("Enter Even or Odd: ")
# for i in input_list:
#     if i % 2 == 0:
#         evenList.append(i)
#     else:
#         oddlist.append(i)
# if user_input == "Even":
#     print(evenList, "Parity: Even")
# elif user_input == 'Odd':
#     print(oddlist, "Parity: Odd")
# else:
#     print("You have input invalid option")


def even_odd_filter(list_of_nums):
    user_input = input("Enter Even or Odd: ")
    evenList = []
    oddlist = []
    for i in list_of_nums:
        if i % 2 == 0:
            evenList.append(i)
        else:
            oddlist.append(i)
    if user_input == "Even":
        print(evenList, "Parity: Even")
    elif user_input == 'Odd':
        print(oddlist, "Parity: Odd")
    else:
        print("You have input invalid option")

even_odd_filter([1,2,3,4,5,6])
