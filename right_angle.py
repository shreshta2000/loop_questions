sum=0
i=1
while i <=3:
	angles = int(input("write angle"))
	
	sum=sum+angles
	i=i+1
print(sum)	
if sum==180:
	if angles==90:
		print("right angle triangle")
	elif angles<90:
		print("obtuse triangle")
	elif angles>90:
		print("acute triangle")
else:
	print("it is not a triangle")

#wrong



