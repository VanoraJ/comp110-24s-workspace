"""Practice with variables and input functions."""

first_name: str = input("What is your name?")
fav_number_str: str = input("What is your favorite number?")
fav_number: int = int(fav_number_str)
higher_number: int = fav_number + 1

print("Hello " + first_name + "!")
print("My favorite number is " + str(higher_number))