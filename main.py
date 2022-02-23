# import os
import replit
import time

def clearSreen():
	# os.system("cls")
	replit.clear()

class MakePlayer:
	def __init__(self, strength, wit, health):
		self.strength = strength
		self.wit = wit
		self.health = health


class UserInterface:
	def playerTurn(self):
		print("Your Turn!!!")
		print("Chose your move: \n \n")
		print("Use stabby stabby boi [1] \n")
		print("Use big brain magic [2] \n")
		print("GO TAKE A NAP AND HEAL!!! [3] \n")

		while True:
			try:
				choice = int(input("Make your selection: "))
				return choice
				break
			except ValueError:
				print('Come on STUPID! I said put in a number!!!(1-3)')

	def roboTurn(self):
		print("Computers Turn!!!")
		time.sleep(2.5)

		


###VARIABLES###	
display = UserInterface()
player1 = MakePlayer(5, 3, 10)
monster = MakePlayer(2, 8, 15)



def game():
	isUser =  True
	while monster.health > 0:
		if isUser:
			display.playerTurn()
			isUser = False
			clearSreen()
		else:
			display.roboTurn()
			isUser = True
			clearSreen()
#testing

game()
