password=input("enter your password  ")
if len(password)==8:
	print("atleast 8 letter in password")
	# print("your password is strong password")
	# break	
	if password>="A" and password<="z":
		print("uppercase in password")
	# break
		if password>="a" and password<="z":
			print("lowercase in password")
			# break
			if "@"in password:
				print("special key in password")
				# break
				if password>="0" and password<="9":
					print("digits in password")
					# # break
					# if len(password)<=8:
					# 	print("atleast 8 letter in password")
					print("your password is strong password")
						# break	
else:
	print("your password is not a strong password")
	# break



