sum=0
number=int(input("enter any number: "))
length=len(str(number))
num=number
while number>0:
	rem=number%10
	digit=rem**length
	number=number//10
	sum=sum+digit
if sum==num:
	print("it is a armstrong number")
else:
	print("it is not a armstrong number")		