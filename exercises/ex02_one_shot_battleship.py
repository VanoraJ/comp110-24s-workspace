"""EX02 - One Shot Battleship."""

__author__ = "730653557"

# Set variables
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

# Emoji
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Ask user to input row
guess_row: int = int(input("Guess a row: "))

# Check if the input row guess is a valid number, if not, guess again
while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Ask user to input column
guess_column: int = int(input("Guess a column: "))

# Check if the input column guess is a valid number, if not, guess again
while guess_column > grid_size or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Set variables for emoji
result: str
row_counter: int = 1

# Determine result
if guess_row == secret_row and guess_column == secret_column:
    result = RED_BOX
else:
    result = WHITE_BOX

while row_counter <= grid_size:
    emoji_str: str = ""
    column_counter: int = 1
    if guess_row == row_counter:
        while column_counter <= grid_size:
            if guess_column == column_counter:
                # Add result box to guessed location
                emoji_str += result
            else:
                # Fill the rest of the row with blue boxes
                emoji_str += BLUE_BOX
            column_counter += 1

    else:
        # If not the guessed row, fill with blue boxes
        while column_counter <= grid_size:
            emoji_str += BLUE_BOX
            column_counter += 1

    print(emoji_str)
    row_counter += 1

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_row != secret_row and guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")