"""Splitting a dictionary into two lists."""

__author__ = "730653557"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Return a list of all the keys of the dinctionary."""
    key_list: list[str] = []
    for keys in dictionary:
        key_list.append(keys)
    return key_list
        

def get_values(dictionary: dict[str, int]) -> list[int]:
    """Return a list of all the vlaues in the dictionary."""
    value_list: list[int] = []
    for keys in dictionary:
        value_list.append(dictionary[keys])
    return value_list