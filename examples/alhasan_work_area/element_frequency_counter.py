element_counter= dict()
list1 = ["alhasan" , "ali", "abbas", "alhasan", "ali", "alhasan"]

for i in list1:
    if i not in element_counter:
        element_counter[i] = 1
    else:
        element_counter[i] +=1
print(element_counter)
