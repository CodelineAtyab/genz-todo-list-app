classic = 'Hello World'
results_list = []
for char in classic:
    if char in ['a', 'e', 'i', 'e', 'o']:
        results_list.append('-')
    else:
        results_list.append(char)
print(''.join(results_list))