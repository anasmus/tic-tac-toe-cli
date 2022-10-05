import os
from random import choice as random_choice
WIDTH = os.get_terminal_size().columns
def main():
  display_guide()
  available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  movelist = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  display_board(movelist)
  while True:
    user_input(available_moves, movelist)
    if not available_moves:
      declare_tie(movelist)
    bot_input(available_moves, movelist)

def user_input(available_moves, movelist):
  print("\n")
  move = 0
  while not move in available_moves:
    try:
      move = int(input("Enter Your Move: "))
    except:
      print("Please Enter a Number corresponding to Your Move")
      move = 0
  update_status(available_moves, movelist, move, "X")

def update_status(available_moves, movelist, current_move, symbol):
  available_moves.remove(current_move)
  movelist[current_move - 1] = symbol
  update_board(movelist)
  check_game(movelist, symbol)

def update_board(movelist):
  cls()
  display_board(movelist)

def check_game(movelist, symbol):
  if movelist.count(symbol) < 3:
    return 
  else:
    winner = check_winner(movelist)
    if winner:
      update_board(movelist)
      print("\n")
      print("You won!".center(WIDTH)) if winner == "X" else print("You lose!".center(WIDTH))
      if (winner == "O"):
        print("You Have Lost from a Bot Making Random Moves".center(WIDTH))
        print("You Must Be Ashamed of Yourself".center(WIDTH))
      print("\n")
      exit(0)

def check_winner(movelist):
  winner = None
  # checking for vertical and horizontal lines
  for i in range(3):
    if (movelist[i] == movelist[i + 3] == movelist[i + 6]):
      winner = movelist[i] if movelist[i] != " " else None
    elif (movelist[3 * i] == movelist[3 * i + 1] == movelist[3 * i + 2]):
      winner = movelist[3 * i] if movelist[3 * i] != " " else None
  # checking for diagonal lines
  if ((movelist[0] == movelist[4] == movelist[8]) or 
          (movelist[6] == movelist[4] == movelist[2])):
    winner = movelist[4] if movelist[4] != " " else None
  
  return winner

def display_guide():
  cls()
  print()
  print()
  print("Welcome Stranger to Tic Tac Toe".center(WIDTH))
  print("You Are Here To Compete With A Bot".center(WIDTH))
  print("Make The Appropriate Moves And Win The Game".center(WIDTH))
  print("Here Are The Moves You Can Make\n".center(WIDTH))
  display_board(range(1,10))
  input("Press Enter to start the game...")
  cls()

def display_board(input_list):
  print(f"-------------".center(WIDTH))
  print(f"| {input_list[0]} | {input_list[1]} | {input_list[2]} |".center(WIDTH))
  print(f"-------------".center(WIDTH))
  print(f"| {input_list[3]} | {input_list[4]} | {input_list[5]} |".center(WIDTH))
  print(f"-------------".center(WIDTH))
  print(f"| {input_list[6]} | {input_list[7]} | {input_list[8]} |".center(WIDTH))
  print(f"-------------".center(WIDTH))

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def declare_tie(movelist):
  update_board(movelist)
  print()
  print("It's a Tie".center(WIDTH))
  print("\n")
  exit(0)

def minimax(available_moves, movelist, user_turn=True):
  move_matrices = []
  winner = check_winner(movelist)
  if winner:
    return 10 if winner == "X" else -10
  if (len(available_moves) == 0):
    return 0

  for move in available_moves:
    remaining_moves = [x for x in available_moves]
    remaining_moves.remove(move)
    new_movelist = [x for x in movelist]
    new_movelist[move - 1] = "X" if user_turn else "O"
    move_matrices.append(minimax(remaining_moves, new_movelist, not(user_turn)))

  return max(move_matrices) if user_turn else min(move_matrices)

def bot_input(available_moves, movelist):
  move_dict = {"value":9999}
  for move in available_moves:
    remaining_moves = [x for x in available_moves]
    remaining_moves.remove(move)
    new_movelist = [x for x in movelist]
    new_movelist[move - 1] = "O"
    move_matrix = minimax(remaining_moves, new_movelist)
    move_dict = {"value": move_matrix, "index": move} if move_matrix < move_dict["value"] else move_dict
    
  move = move_dict["index"]
  print(f"Bot Played {move}")
  input("Press any key to continue...")
  update_status(available_moves, movelist, move, "O")

if __name__ == "__main__":
  main()