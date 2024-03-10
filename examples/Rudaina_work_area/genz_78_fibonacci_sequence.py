def fibonacci_sequence_generator(n):
    lst = [0, 1]
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
        while lst[-1] + lst[-2] < n:
            lst.append(lst[-1] + lst[-2])
    return lst
    
print(fibonacci_sequence_generator(5))
            
        