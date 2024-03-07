def element_frequency(reccur):
    frequency = {}
    for element in reccur:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
            pass
    return frequency

food_list = ['burger','pie','burger','burger','orange','pie']
frequency = element_frequency(food_list)
print(frequency)

{"burger": 1, "pie": 1}