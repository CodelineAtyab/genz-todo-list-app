value = int(input("Please enter the number of lines: "))

def pali_structure(value):
    x=""
    for i in range(1,value+1):
        x = x + "1"
        space = " " * (value-i)
        print(space, (int(x) * int(x)))
    
pali_structure(value)
