def fibonacci(no_elements):
    seq = []
    count, first_element , second_element = 0, 0 , 1
    if no_elements == 0:
        return 0
    elif no_elements == 1:
        return 1
    else:
        while count < no_elements:
            seq.append(first_element)
            count += 1
            next_element = first_element + second_element
            first_element = second_element
            second_element = next_element
        return seq
    
print(fibonacci(7))