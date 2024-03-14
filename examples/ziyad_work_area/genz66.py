n = int(input("Enter n: "))

result = [0, 1]
first_num = result[0]
second_num = result[1]

for i in range(n):
    if n == 0:
        result = []
    elif n == 1:
        result = [0]
    elif n >= 2:
        next_num = first_num + second_num
        result.append(next_num)
        first_num = second_num
        second_num = next_num

print(result)