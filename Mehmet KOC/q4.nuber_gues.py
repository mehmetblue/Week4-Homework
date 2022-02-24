"""
4) Number Guessing Game

General Information:
I want to play a game which I can guess a number. 
The computer chooses a number in the range I chose. 
So that I can try to find the correct number which was selected by computer.

Acceptance Criteria:
* Computer must randomly pick an integer from user selected a range, 
i.e., from A to B, where A and B belong to Integer. 
* Your program should prompt the user for guesses if the user guesses incorrectly, 
it should print whether the guess is too high or too low. 
* If the user guesses correctly, the program should print total time and total number of guesses. 
* You must import some required modules or packages You can assume that the user will enter valid input.

"""

import random
import timeit


## recording the beginning of the execute time
start = timeit.default_timer()


## taking the lower bound with input
lower = int(input("Please type the lower bound: "))


## taking the upper bound with input
upper = int(input("Please type the upper bound: "))


## generating random number between
# the lower and upper bound
x = random.randint(lower, upper)


# initializing the number of guesses.
attempt = 0


while True:


	## getting guessing number as input
	guess = int(input("Guess a number: "))
	attempt += 1


	## condition testing
	if x > guess:
		print("The guess is too low!")


	elif x < guess:
		print("The guess is too high!")


	else:
		## two different message, if the user guess 
		# the number on first attempt and others
		if attempt == 1:
			print("\nThe number is", x)
			print("Wow! You guess the number on the first attempt.")
		else:
			print("\nThe number is", x)
			print("Yes. You guess the number in",
				attempt, "attempts.")		


		## recording the ending of the execute time
		end = timeit.default_timer()


		## total elapsed time
		elapsed_time = int(end-start)

		## displays the elapsed time
		print(f"Your elapsed time is", elapsed_time, "seconds.\n")
		break