number=5
print("you have to guess number 1 to 10")
chance=5
while chance>=1:
	user_guess=int(input("enter your guessed number "))
	if number==user_guess:
		print("you guessed right number",user_guess,"you win")
		break
	elif number<user_guess:
		print("you guessed greater than number")
	else:
		print("you guessed smaller than number")
	chance=chance-1
	print("you have chance",chance)
else:
	print("you lose your game")