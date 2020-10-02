# Codecademy - Python
# Implementation of Battleship Game Project(Codecademy - Python)
# for reference to walk throw  vedio in link blow
# (1) https://youtu.be/waTN4mBWMtA
# (2) https://youtu.be/W8Dx5_siqNI
# (3) https://youtu.be/MjTJl3b-zzI

board = []  # Empty List named board

# create 5 *5 board 
for i in  range(0, 5) :
  board.append(['O'] * 5) # bulid 5*5 board
  # print(['O'] * 5)

#print (board) # for testing

# Custom function to print board
def print_board( board) :
  # print row by row
  # iterate over (2 d array) and join the rows 
  # then print so output will be little nice
  for row in board :
     print(' '.join(row))

# call print_board function
print_board(board)

# include randint function (will give us random int numbers)
from random import randint 

# Place Hiddden item in random Place
#random_row = randint(0, len(board) - 1)   # get random number for row
#random_column = randint(0, len(board) - 1) # get random number for column
#board[random_row][random_column] = "HIDDEN ITEM"

# random row function
def random_row(board) :
  return randint(0, len(board))

# random column function
def random_column(board) :
  return randint(0, len(board))

# call functions
ship_row =    random_row(board)   # get random number for row
ship_column = random_column(board)  # get random number for column

print(ship_row) # for testing
print(ship_column) # for testing
alowed_guess = 4   # user sholud have only have 4 guess
guess = 0  # guess  so far

# all the code logic need to be Loop
while guess < 4 :

  # get input from User
  guess_row = int(input("Gues Row : "))
  guess_column = int(input("Gues Column : "))

  #print(ship_row) # only for testing
  #print(ship_column) # only for testing

  # time for winner now
  # Handle all the corner cases
  # this check if you guessed correctly
  if guess_row == ship_row and guess_column == ship_column :
    # if user ques was right
    print("Congratulation ! You snak my battleship!")
    break # we are done

  # this check if you guessed  with the 5* 5 grid
  elif guess_row not in range(5) or guess_column  not in range(5) :
    print("You Guessed Outside of the board")
    print("Oops, that's not even in the ocan.")

  # if user Enter which allready been guessed
  # this check if you allready guessed in that location
  elif board[guess_row][guess_column] == "X" :
    print("You gussed that one allready!")

  else : # else caese  if you not guessed correctly
    print("You Missed my battleship")
    # change board[guess_row][guess_column] to X
    board[guess_row][guess_column] = "X"
    # call print_board function
    print_board(board)
    guess += 1 # increment guese by one

    # this check if you run out of guess
    if guess == alowed_guess:
      print("Game is Over You finished All number Guess")
    else :
      print("You have left with ", alowed_guess - guess) 
  

