#************Global variable********

# Game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#if game is stillgoing
game_still_going = True

# Who won? or tie?
winner = None

# Whos turn is it
current_player = "X" 

def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
  #display box
  display_board()

  while game_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()

    #the game has ended
  if winner == "X" or winner == "O":
    print(winner + "won.")
  elif winner == None:
    print("Tie.")  



def handle_turn(player):
  print(player + "'s turn. ")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] :
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You cant go there. Go again. ")

  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  #set up globa variables
  global winner

  #check row
  row_winner = check_rows()
  #check colunm
  column_winner = check_column()
  #check diagonals
  diagonal_winner = check_diagonals()

  #get the winner
  if row_winner:
    winner = row_winner
    #there was a win
  elif diagonal_winner:
    winner = diagonal_winner
    #there was a win
  elif column_winner:
    winner = column_winner
    #there was a win
  else:
    winner = None
    #there was no win
  return

def check_rows():
  #set up global variable
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_column():
  global game_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"
  if diagonals_1 or diagonals_2 :
    game_still_going = False
  if diagonals_1:
    return board[0]
  elif diagonals_2:
    return board[6]
  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  
  return

def flip_player():
  # global variables we need
  global current_player
  # if the current player x, then change it to 0
  if current_player == "X":
    current_player = "O" 
    # if the current_player o, then changr it to x
  elif current_player == "O":
    current_player = "X"
  return

play_game()
