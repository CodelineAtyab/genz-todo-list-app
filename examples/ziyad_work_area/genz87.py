input = [1, 2, 4, 5]

expected_sum = 0
for i in range(input[0], input[-1] + 1):
    expected_sum = expected_sum + i

actual_sum = 0
for i in input:
    actual_sum = actual_sum + i

print(expected_sum - actual_sum)