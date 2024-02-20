"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730653557"

Blue_box: str = "\U0001F7E6"
Red_box: str = "\U0001F7E5"
White_box: str = "\U00002B1C"

player_1_location_str: str = input("Pick a secret boat location between 1 and 4: ")
player_1_location_int: int = int(player_1_location_str)

if player_1_location_int < 1:
    print(f"Error! {player_1_location_int} too low!")
    exit()
if player_1_location_int > 4:
    print(f"Error! {player_1_location_int} too high!")
    exit()

player_2_guess_str: str = input("Guess a number between 1 and 4: ")
player_2_guess_int: int = int(player_2_guess_str)

if player_2_guess_int < 1:
    print(f"Error! {player_2_guess_int} too low!")
    exit()
if player_2_guess_int > 4:
    print(f"Error! {player_2_guess_int} too high!")
    exit()

result: str

if player_2_guess_int == player_1_location_int:
    result = Red_box
else:
    result = White_box

emoji_str: str = ""

emoji_str = emoji_str + (result if player_2_guess_int == 1 else Blue_box)
emoji_str = emoji_str + (result if player_2_guess_int == 2 else Blue_box)
emoji_str = emoji_str + (result if player_2_guess_int == 3 else Blue_box)
emoji_str = emoji_str + (result if player_2_guess_int == 4 else Blue_box)

if player_2_guess_int == player_1_location_int:
    print(emoji_str) 
    print("Correct! You hit the ship.")
else:
    print(emoji_str) 
    print("Incorrect! You missed the ship.")