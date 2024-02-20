"""EX03 - Functional Battleship."""

__author__ = "730653557"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, specify: str) -> int:
    """Part1: defining the function input_guess: used to get the guesses within the grid boundaries."""
    assert specify == "row" or specify == "column"
    guess = int(input(f"Guess a {specify}: "))
    while guess > grid_size or guess < 1:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, correctness: bool) -> None:
    """Part2: defining the function print_grid: compare with the secrets, and print out the emoji grid."""
    row_counter: int = 1

    while row_counter <= grid_size:
        emoji_str: str = ""
        column_counter: int = 1

        while column_counter <= grid_size:
            if row_counter == row_guess and column_counter == column_guess:
                if correctness:
                    emoji_str += RED_BOX
                else:
                    emoji_str += WHITE_BOX
            else:
                emoji_str += BLUE_BOX
            
            column_counter += 1
        
        print(emoji_str)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Part3: defining the function correct_guess: check if the guess is correct, return white or red box."""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Part4: defining the function main: combining everything."""
    max_turn: int = 5
    turn_counter: int = 1
    winning: bool = False

    while turn_counter <= max_turn and not winning:
        print(f"=== Turn {turn_counter}/{max_turn} ===")

        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")

        if correct_guess(secret_row, secret_column, row_guess, column_guess):
            print("Hit!")
            print(f"You won in {turn_counter}/{max_turn} turns!")
            print_grid(grid_size, row_guess, column_guess, True)
            winning = True
            return None
        else:
            print("Miss!")
            print_grid(grid_size, row_guess, column_guess, False)

        turn_counter += 1

    if not winning:
        print(f"X/{max_turn} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))