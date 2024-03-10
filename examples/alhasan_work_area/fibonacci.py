def fibonacci(series):
    a = 0
    b = 1
    if series == 0:
        return []
    elif series == 1:
        return [0]
    else:
        result = [0,1]
        for i in range(series):
            c = a + b
            result.append(c)
            a = b
            b = c    
        return result

print(fibonacci(10))   