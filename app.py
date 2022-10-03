import os
WIDTH = os.get_terminal_size().columns
def main():
  display_guide()

def display_guide():
  cls()
  print()
  print()
  print("Welcome Stranger to Tic Tac Toe".center(WIDTH))
  print("You Are Here To Compete With A Bot".center(WIDTH))
  print("Make The Appropriate Moves And Win The Game".center(WIDTH))
  print("Here Are The Moves You Can Make\n".center(WIDTH))
  update_board(range(1,10))

def update_board(input_list):
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