import os
WIDTH = os.get_terminal_size().columns
def main():
  display_guide()
  available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  display_board(board)
  while True:
    user_input(available_moves, board)
    if not available_moves:
      declare_tie(board)
    bot_input(available_moves, board)

def user_input(available_moves, board):
  print("\n")
  move = 0
  while not move in available_moves:
    try:
      move = int(input("Enter Your Move: "))
    except:
      print("Please Enter a Number corresponding to Your Move")
      move = 0
  update_status(available_moves, board, move, "X")

def update_status(available_moves, board, current_move, symbol):
  available_moves.remove(current_move)
  board[current_move - 1] = symbol
  update_board(board)
  check_game(board, symbol)

def update_board(board):
  cls()
  display_board(board)

def check_game(board, symbol):
  if board.count(symbol) < 3:
    return 
  else:
    winner = check_winner(board)
    if winner:
      update_board(board)
      print("\n")
      print("You won!".center(WIDTH)) if winner == "X" else print("You lose!".center(WIDTH))
      print("\n")
      exit(0)

def check_winner(board):
  # checking for vertical lines
  for i in range(3):
    if (board[i] == board[i + 3] == board[i + 6] == "X"):
      return "X"
    elif (board[i] == board[i + 3] == board[i + 6] == "O"):
      return "O"

  # checking horizontal lines
  for i in [0, 3, 6]:
    if (board[i] == board[i + 1] == board[i + 2] == "X"):
      return "X"
    elif (board[i] == board[i + 1] == board[i + 2] == "O"):
      return "O"

  # checking for diagonal lines
  if (board[0] == board[4] == board[8] == "X"):
    return "X"
  elif (board[0] == board[4] == board[8] == "O"):
    return "O"
  elif (board[6] == board[4] == board[2] == "X"):
    return "X"
  elif (board[6] == board[4] == board[2] == "O"):
    return "O"
  
  # if nothing matches
  return None

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

def declare_tie(board):
  update_board(board)
  print()
  print("It's a Tie".center(WIDTH))
  print("\n")
  exit(0)

def minimax(available_moves, board, user_turn=True):
  move_matrices = []
  winner = check_winner(board)
  if winner:
    return 10 if winner == "X" else -10
  if (len(available_moves) == 0):
    return 0

  for move in available_moves:
    remaining_moves = [x for x in available_moves]
    remaining_moves.remove(move)
    new_board = [x for x in board]
    new_board[move - 1] = "X" if user_turn else "O"
    move_matrices.append(minimax(remaining_moves, new_board, not(user_turn)))

  return max(move_matrices) if user_turn else min(move_matrices)

def bot_input(available_moves, board):
  move_dict = {"value":9999}
  for move in available_moves:
    remaining_moves = [x for x in available_moves]
    remaining_moves.remove(move)
    new_board = [x for x in board]
    new_board[move - 1] = "O"
    move_matrix = minimax(remaining_moves, new_board)
    move_dict = {"value": move_matrix, "index": move} if move_matrix < move_dict["value"] else move_dict
    
  move = move_dict["index"]
  print(f"Bot Played {move}")
  input("Press any key to continue...")
  update_status(available_moves, board, move, "O")

if __name__ == "__main__":
  main()