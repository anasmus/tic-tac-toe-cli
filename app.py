import os
from random import choice as random_choice
WIDTH = os.get_terminal_size().columns
def main():
  display_guide()
  available_moves = [x for x in range(1,10)]
  movelist = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  display_board(movelist)
  while True:
    user_input(available_moves, movelist)
    update_board(movelist)
    if not available_moves:
      break
    bot_input(available_moves, movelist)
    update_board(movelist)

def user_input(available_moves, movelist):
  print("\n")
  move = 0
  while not move in available_moves:
    try:
      move = int(input("Enter Your Move: "))
    except:
      print("Please Enter a Number corresponding to Your Move")
      move = 0
  available_moves.remove(move)
  movelist[move - 1] = "X"

def bot_input(available_moves, movelist):
  move = random_choice(available_moves)
  available_moves.remove(move)
  movelist[move - 1] = "O"
  print(f"Bot Played {move}")
  input("Press any key to start the game...")

def update_board(movelist):
  cls()
  display_board(movelist)

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

if __name__ == "__main__":
  main()