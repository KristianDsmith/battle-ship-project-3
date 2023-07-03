# Rules
# X fr placing ship and hit battleship
# ' ' for availble space
# '-' for missed shot

from random import randint

#board for hlding ship locations

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

# Board for displaying hits and misses

GUESS_BOARD = [[" "] * 8 for x in range(8)]

# The output of this function would make a game board in a grid format.
# Row numbers on the left and column labels on the top.
# The contents of the board are displayed 
# Using "|" separators between each element.

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_numbers += 1

# Convert letters to numbers
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# Computer creates 5 ships
# 5 ships are randomly placed on the game board represented by the board parameter.
def create_ships(board)
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
            board[ship_row][ship_column] = "X"