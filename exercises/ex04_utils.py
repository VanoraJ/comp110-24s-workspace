"""Exercise 04 - List utility functions."""

__author__ = "730653557"


def all(my_list: list[int], number: int) -> bool:
    """Returns False if there is nothing in the list."""
    if len(my_list) == 0:
        return False

    """Function checks if the numbers in the list matches with the target given number."""
    idx: int = 0
    while idx < len(my_list):
        if my_list[idx] != number:
            return False
        idx += 1

    return True
            

def max(my_list: list[int]) -> int:
    """Return ValueError if the list is empty."""
    if len(my_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    """Function returns the largest int in the list"""
    idx: int = 0
    max_num: int = my_list[0]
    while idx < len(my_list):
        current_num: int = my_list[idx]
        if current_num > max_num: 
            max_num = current_num
        idx += 1
    
    return max_num


def is_equal(l1: list[int], l2: list[int]) -> bool:   
    """First check - whether length matches?"""
    if len(l1) != len(l2):
        return False
    
    """Second check - whether all number at each idx is the same?"""
    idx: int = 0
    while idx < len(l1):
        if l1[idx] != l2[idx]:
            return False
        idx += 1

    return True


def extend(l1: list[int], l2: list[int]) -> None:
    """Function goes through all idx of list 2 and append them to the end of list 1."""
    idx: int = 0
    while idx < len(l2):
        l1.append(l2[idx])
        idx += 1