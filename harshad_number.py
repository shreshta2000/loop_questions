number=int(input("enter any nuber"))
sum=0
while number>0:
	rem=number%10
	sum=sum+rem
	number=number//10
if number%sum==0:
	print("it is a harshad number")
else:
	print("it is not a harshad number")
