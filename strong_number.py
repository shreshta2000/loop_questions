sum=0
factorial=1
i=0
number=int(input("enter number"))
while i<=number:
	factorial=(number%10)*factorial*i
	sum=sum+factorial
	if sum==number:
		print("it is a strong number",number)
	else:
		print("it is not a strong number",number)
	i=i+1



	