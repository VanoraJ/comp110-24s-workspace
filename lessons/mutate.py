"""Mutating functions."""

__author__ = "730653557"


def manual_append(my_list: list[int], number: int) -> None:
    """The function will append the int parameter to the end of the list[int] parameter."""
    my_list.append(number)


def double(my_list: list[int]) -> None:
    """The function will multiply every element in the list[int] parameter by 2."""
    index: int = 0
    while index < len(my_list):
        my_list[index] = my_list[index] * 2
        index += 1