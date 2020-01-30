"""
Python algorithm for a mancal robot with an
Alpha Beta Pruning strategy

Extremely rough by the way
"""

import math

def miniMax(board, depth, player):
	"""
	This function computes the future moves on the board for a player and returns
	the move with the best score after a certain depth
	"""

	#Maximize the score for this player. Other player is minimized
	maximizePlayer = player
	#Number of move
	move = -1
	#Score representing utility of move
	score = -math.inf

	if (board[1] + board[3]) == 0:
		return (-1, -1)

	if depth == 0:
		return bestMove(board, -1)

	"""
	Traverse through possible moves return the score based
	on bestMove() and minimize or maximize based on the player
	"""
	#nextMove(board)
	
	"""
	return the best move for the maximizing or minimizing player
	"""
	 

	return move

def nextMove(board):
	#TODO - specify player to choose move for
	nextMove = 0
	nextBoard = board
	score = 0

	#Holds all the non-empty buckets or possible moves
	moves = []

	#Represents the current bucket being checked
	bucket = 0

	#Loops through all of player 1 buckets
	for marbles in board[1]:
		#If the bucket is not empty then add bucket to list of possible moves
		if marbles != 0:
			moves.append(bucket)
		#Check next bucket
		bucket += 1

	#Loop through non-empty spots
	for move in moves:
		#Check if non-empty spot belongs to player 1
		if(move <= 6)
			#Spot to deposit next marble
			spot = move + 1
			#Number of marbles retrieved from spot
			marbles = nextBoard[1][move]
			#Deposit marbles until none left
			while marbles > 0:
				if spot < 6:
					#Spot is player 1's mancala
					if spot == 6:
						nextBoard[0] + 1
					#Add one to the next player 1 spot
					nextBoard[1][spot] += 1
					marbles - 1
					spot + 1
				else:
					#Spot is player 2's mancala
					if spot == 12:
						nextBoard[2] += 1
					#Add one to the next player 2 spot
					nextBoard[3][spot] += 1
					marbles -1
					spot + 1
		"""			
		if the heuristic for current move is highest replace score,
		replace move and repeat loop
		"""
		if bestMove(nextBoard) > score:
			score = bestMove(nextBoard)
			nextMove = move







	
def bestMove(board):
	"""
	This function calculates the utility of the current
	chosen move and returns the score for the move. The
	higher the number the better the move.
	"""

	#TODO - Represent a player ID so that the AI can play as either player 

	#Represent the players current ampount marble 
	p1_marbles = 0
	p2_marbles = 0

	#Count marbles in both players bucket's
	for marbles in board[1]:
		p1_marbles += marbles

	for marbles in board[3]:
		p2_marbles += marbles

	"""
	Add the marbles within each players mancalas with a double value
	to represent the fact that these marbles cannot be moved
	"""
	p1_marbles += board[0]*2
	p2_marbles += board[0]*2

	"""
	Return the utility of a move by checking how many 
	marbles a  player versus the opponent
	"""
	return p1_marbles - p2_marbles
	

def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, 
				 	player2Marbles):
	
	#Represent all the values on the board
	board = [player1Mancala, player1Marbles, player2Mancala, player2Marbles]

	#Amount of moves we would like to search
	depth = 3

	#Call a function to look a certain amount of moves ahead
	miniMax(board, depth, player)