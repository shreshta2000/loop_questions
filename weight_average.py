sum=0
average=0
i=1
while i<=11:
	weight=int(input("enter any number"))
	sum=sum+weight
	i=i+1
print("sum",sum)
average=sum/11
if average!=0:
	print("average",average)
	if average%5==0:
		print("average is divisible by 5",average)
	else:
		print("average is not divisible by 5",average)
	# average=sum/11
	# if average!=0:
	# 	if sum%5==0:
	# 		i=i+1
	# 		print("average is divisible by 5")
	# 	else:
	# 		print("average is not divisible by 5")

	# 