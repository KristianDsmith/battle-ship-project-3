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