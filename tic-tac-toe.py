# tic tac toe game  

board = [] 
for i in range(9):
	board.append(" ")


def print_board():
	print()
	c = 0
	while c < 9:
		print(board[c] + " | " + board[c+1] + " | " + board[c+2])
		if c < 6:
			print("--+---+--")
		c = c + 3
	print()


# made this list manually, these are the only ways to win
winning_combinations = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 4, 6]
]


def check_winner(player):
	for combo in winning_combinations:
		a = combo[0]
		b = combo[1]
		c = combo[2]
		if board[a] == player and board[b] == player and board[c] == player:
			return True
	return False


def is_draw():
	for spot in board:
		if spot == " ":
			return False
	return True


#minimax - ai is O (tries to get highest score), human is X (tries to get lowest)
def minimax(isaiturn):
	if check_winner("O"):
		return 1
	if check_winner("X"):
		return -1
	if is_draw():
		return 0

	if isaiturn:
		best = -999
		for c in range(9):
			if board[c] == " ":
				board[c] = "O"
				score = minimax(False)
				board[c] = " "
				if score > best:
					best = score
		return best
	else:
		best = 999
		for c in range(9):
			if board[c] == " ":
				board[c] = "X"
				score = minimax(True)
				board[c] = " "
				if score < best:
					best = score
		return best


def ai_move():
	best_score = -999
	best_move = -1

	for c in range(9):
		if board[c] == " ":
			board[c] = "O"
			score = minimax(False)
			board[c] = " "

			if score > best_score:
				best_score = score
				best_move = c

	board[best_move] = "O"


def human_move():
	while True:
		move = input("Enter position (1-9): ")

		if not move.isdigit():
			print("Please enter a valid number (1-9).")
			continue

		move = int(move)
		move = move - 1

		if move < 0 or move > 8:
			print("Please enter a valid number (1-9).")
			continue

		if board[move] != " ":
			print("That spot is already taken, try again.")
			continue

		board[move] = "X"
		break


print("Welcome to Tic Tac Toe!")
print("You are X, computer is O")
print("Goodluck (you'll probably need it lol)")

game_running = True

while game_running:
	print_board()
	human_move()

	if check_winner("X"):
		print_board()
		print("You win! nice job")
		game_running = False
		continue

	if is_draw():
		print_board()
		print("It's a draw!")
		game_running = False
		continue

	print()
	print("computer is thinking...")
	ai_move()

	if check_winner("O"):
		print_board()
		print("computer wins, better luck next time")
		game_running = False
		continue

	if is_draw():
		print_board()
		print("It's a draw!")
		game_running = False
		continue
