from random import randint

# Battleships Game
# Rules:
# - The game is played on an 8x8 grid.
# - The computer randomly places 5 ships on the grid.
# - Destroy all the computer's ships by guessing their locations.
# - On each turn, enter a row and column to guess the ship location.
# - If your guess is a hit, the position on the guess board will show 'X'.
# - If your guess is miss, the position on the guess board will show '-'.
# - You have a total of 10 turns to sink all the ships.
# - The game ends when you either sink all the ships or run out of turns.
# - Enter your guess, input the row and column with format 'A1' to 'H8'.
# - If invalid row or column, you are prompted to enter a valid choice.
# - prompted to enter a valid choice.
# - You cannot guess the same position multiple times.
# - showing your hits, misses, and remaining turns.
# - Good luck!

# Print the rules for the player to read
print("Welcome to Battleships!")
print("Rules:")
print("-" * 50)
print("The game is played on an 8x8 grid.")
print("The computer randomly places 5 ships on the grid.")
print("Destroy all the computer's ships by guessing their locations.")
print("On each turn, enter a row and column to guess the ship location.")
print("If your guess is a hit, the position on the guess board will show 'X'.")
print("If your guess is miss, the position on the guess board will show '-'.")
print("You have a total of 10 turns to sink all the ships.")
print("The game ends when you either sink all the ships or run out of turns.")
print("Enter your guess, input the row and column with format 'A1' to 'H8'.")
print("If invalid row or column, you are prompted to enter a valid choice.")
print("You cannot guess the same position multiple times.")
print("The grid will be displayed after each guess.")
print("showing your hits, misses, and remaining turns.")
print("Good luck!")


# board for holding ship locations.
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

# Board for displaying hits and misses

GUESS_BOARD = [[" "] * 8 for i in range(8)]

# The output of this function would make a game board in a grid format.
# Row numbers on the left and column labels on the top.
# The contents of the board are displayed.
# Using "|" separators between each element.


def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


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
# 5 ships are randomly placed on game board represented by the board parameter.
def create_ships(board):
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
    board[ship_row][ship_column] = "X"

# User input lacation on board


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in ["1", "2", "3", "4", "5", "6", "7", "8"] or row == "":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while (
        column not in ["A", "B", "C", "D", "E", "F", "G", "H"] or column == ""
    ):
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

# Check if all ships are hit


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

# Overall gameplay


if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")