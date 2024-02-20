"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of 2 numbers"""
    if number1 >= number2:
        return number1
    else: # number1 < number 2
        return number2

my_max_number: int = my_max(3, 6)
print(my_max_number)

other_max_number: int = my_max(11, 3)
print(other_max_number)