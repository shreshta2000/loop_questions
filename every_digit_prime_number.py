number=int(input("enter any number"))
while number>0:
	i=2
	rem=number%10
	while i<rem:
		if rem%i==0:
			print("not prime",rem)
			break
		elif rem==1:
			print("not a prime",rem)
			break
		else:
			print("prime",rem)
			break
			i=i+1
	number=number//10
