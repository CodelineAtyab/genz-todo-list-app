def fibonacci_sequence(n):
    res = []
    if n == 0:
        res = [0]
    elif n == 1: 
        res = [0,1]
    else:
        res = [0,1]
        for i in range(2, n):
            res.append(res[i-1] + res[i-2])
    return res 

    