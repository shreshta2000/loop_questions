num1 = int(input("enter any number"))
num2 = int(input("enter any number"))
if(num1 > num2 ):    
    max= num1
else:
    max= num2
while max>=0:
    if(max % num1 == 0 and max % num2 == 0):   
        print("lcm is",max)
        break
    max= max+ 1