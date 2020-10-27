num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
if num1>num2:
	max=num1
else:
	max=num2
i=1
while i <=max:
  if(num1 % i == 0 and num2 % i == 0):
    hcf= i
  i = i + 1
print("hcf is", hcf)
