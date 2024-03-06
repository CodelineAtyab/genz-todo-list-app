list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[]
odd_numbers=[]

for n in list_of_numbers:   
    if n % 2 == 0:        
        even_numbers.append(n)    
    else:
        odd_numbers.append(n) 

  

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
