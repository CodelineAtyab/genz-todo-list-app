"""
 A program that acts as an XOR swapper
"""

def XOR_swapper(value1 , value2):
    x = value1 ^ value2
    value1 = x ^ value1
    value2 = x ^ value2
    print(f"First value is: {value1} Second value is: {value2}")

XOR_swapper(1,3)

# def XOR_swapper(value1 , value2):
#     value1, value2 = value2, value1
#     print(f"First value is: {value1} Second value is: {value2}")

# XOR_swapper(1,3)
