from random import randint
import os

os.system("clear")

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print("__________         __    __  .__                .__    .__        ")
print("\______   \_____ _/  |__/  |_|  |   ____   _____|  |__ |__|_____  ")
print(" |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___/  |  \|  \____ \ ")
print(" |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >")
print(" |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/ ")
print("        \/      \/                     \/     \/     \/   |__|    ")

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    break   
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if turn == 3:
      print("Game Over")
      board[ship_row][ship_col] = "S"
    print_board(board)