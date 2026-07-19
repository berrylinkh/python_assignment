Rock_Paper_Scissor ="""

		 selection list

		 rock
		 paper
		 scissor
		"""
print(Rock_Paper_Scissor)
player_one = str(input("enter option: "))
player_two = str(input("enter option: "))

if player_one == player_two:
	print ("Tie")

elif player_one == "rock" and player_two == "scissor":
	print ("Player one wins")


elif player_one == "paper" and player_two == "rock":
		print ("Player one wins")


elif player_one == "scissor" and player_two == "paper":
		print ("Player one wins")

elif player_one == "rock" and player_two == "paper":
		print ("Player one wins") 
