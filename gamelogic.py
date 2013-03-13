from RPS1 import *
import time, math, random


def computer_strategy():
	"""Returns the computer's move, computed naively."""
	all_moves = ["rock", "paper", "scissors"] #all possible moves
	temp= int(math.floor(random.random() * 3))
	return all_moves[temp]



def determine_winner(p1_choice, p2_choice):
	"""
	Takes in the choices of two players and returns object that one that round.  If both players chose the same
	object, the method returns 'same'
	"""

	if (p1_choice == None or p2_choice == None):
		return "Error choosing data"	

	if p1_choice == p2_choice:
		return "same"

	choices = [p1_choice, p2_choice]
	#paper beats rock
	if "rock" in choices and "paper" in choices:
		return "paper"
	#rock beats scissors
	elif "rock" in choices and "scissors" in choices:
		return "rock"
	#scissors beats paper
	elif "scissors" in choices and "paper" in choices:
		return "scissors"
	 

def play_computer(score_to_win,p1_score, p2_score, listener, controller):
	"""The only game mode currently working."""
	
	#ensure that no one has surpassed the winning score yet.
	while p1_score < score_to_win and p2_score < score_to_win:

		#delay is necessary to give players a chance to throw, or else Leap Motion will detect instantaneously.
		time.sleep(2)
		print("Chose your object now!")
		time.sleep(1)
		#obtain choice from the Leap Motion.
		player_choice = play_alone(listener, controller)
		print "    You chose " + player_choice
		#obtain computer's choice randomly.
		computer_choice = computer_strategy()
		print "    Computer chose " + computer_choice
		#change score
		p1_score, p2_score = change_score(player_choice, computer_choice, p1_score, p2_score)

	if p1_score > p2_score:
		print "Player 1 wins!"
	else:
		print "Computer wins!"
	# The controller must be disposed of before the listener
	controller = None

def change_score(p1_choice, p2_choice, p1_score, p2_score):
	"""Updates the winning player's score"""

	winning_object = determine_winner(p1_choice, p2_choice)

	if winning_object != 'same':
		print "\t" + winning_object.capitalize() + " wins."
	if winning_object == p1_choice:
		p1_score += 1
	elif winning_object == p2_choice:
		p2_score +=1
	else:
		print "You both chose the same object!"
	print "Current score:  Human: " + str(p1_score) + " Computer: " + str(p2_score)
	return p1_score, p2_score


def admin():
	print "Let's play Rock, Paper, Scissors!"
	# Create a sample listener and assign it to a controller to receive events
	listener = RPSListener()
	controller = Leap.Controller(listener)

	#instantiate response
	response = None

	#infinite loop because return will automatically exit when something is returned
	while True:
		print "What score would you like to play to?"
		#Wait statements are horrible, but we need to wait so the user can read the prompt and decide on what to do.
		time.sleep(2)
		score_to_win = average_num_fingers(listener, controller)
		print "Play up to " + str(score_to_win)
		#call game logic, and pass in our score to win, both player's initial scores, the listener and the controller.
		play_computer(score_to_win, 0, 0, listener, controller)