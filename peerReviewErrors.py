# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Jason Palomo
# Creation Date: 07/23/2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#	print('''You are in a land full of dragons. In front of you,
#	you see two caves. In one cave, the dragon is friendly
#	and will share his treasure with you. The other dragon
#	is greedy and hungry, and will eat you on sight.''')
#	print()

	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n''')
#	print()
#Added a new line at the end of the text. No need for empty print and fixed
#the indentions of the display so it lines up nice. 

#def chooseCave():
#    cave = ''
#	while cave != '1' and cave != '2':
#  	cave = input("Which cave will you go into? (1 or 2) \n")
#		return cave

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		cave = input("Which cave will you go into? (1 or 2) \n")
		return cave
#Incorrect indents fixed, combined the text choice into one line with input command.ArithmeticError
#Added a new line in the input so you dont needa blank print

def checkCave(chosenCave):
	
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...\n')
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
    	#print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!') #Print was missing ()

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y': #fixed = to == so it was a comparison and not assigning
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	playAgain = input('Do you want to play again? (yes or no)\n')
	if playAgain == "no":
		print("Thanks for playing")
