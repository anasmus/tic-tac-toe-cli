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

def bot_input(available_moves, movelist):
  move = random_choice(available_moves)
  print(f"Bot Played {move}")
  input("Press any key to continue...")
  update_status(available_moves, movelist, move, "O")

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
    win = False
    # checking for vertical and horizontal lines
    for i in range(3):
      if ((movelist[i] == movelist[i + 3] == movelist[i + 6]) or 
          (movelist[3 * i] == movelist[3 * i + 1] == movelist[3 * i + 2])):
        win = True
    # checking for diagonal lines
    if ((movelist[0] == movelist[4] == movelist[8]) or 
            (movelist[6] == movelist[4] == movelist[2])):
      win = True
    if win:
      update_board(movelist)
      print("\n")
      print("You won!".center(WIDTH)) if symbol == "X" else print("You lose!".center(WIDTH))
      if (symbol == "O"):
        print("You Have Lost from a Bot Making Random Moves".center(WIDTH))
        print("You Must Be Ashamed of Yourself".center(WIDTH))
      print("\n")
      exit(0)

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
  update_board()
  print()
  print("It's a Tie".center(WIDTH))
  print("\n")
  exit(0)

if __name__ == "__main__":
  main()