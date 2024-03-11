a = int(input("a= "))
b = int(input("b= "))

#the follwing will turn the inputs into binary and then swap them
a = a ^ b 
b = a ^ b
a = a ^ b 

print("a= ", a, ",", "b= ", b)