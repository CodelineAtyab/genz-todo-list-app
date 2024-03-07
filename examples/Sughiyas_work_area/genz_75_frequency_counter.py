def count_occurr(input_list):
    word_count = {}

    for word in input_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

my_list = ["apple", "orange", "banana", "apple", "orange", "apple","cherry"]
result = count_occurr(my_list)
print(result)
