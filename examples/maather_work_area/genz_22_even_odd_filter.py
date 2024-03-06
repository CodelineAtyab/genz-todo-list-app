
def even_odd_filter(nums, parity):
    evens = []
    odds  = []
    for num in nums:
        if (num % 2 == 0):
            evens.append(num)
        else:
            odds.append(num)
    if parity.lower() == "even":
        return evens
    else:
        return odds


# example
print(even_odd_filter([1, 2, 3, 4, 5, 6],"odd"))
