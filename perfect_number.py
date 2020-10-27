number=int(input("enter any number"))
sum=0
i=1
while i<number:
	if number%i==0:
		sum=sum+i
	i=i+1
if sum==number:
	print("it is a perfect number",sum)
else:
	print("it is not a perfect number",sum)
			