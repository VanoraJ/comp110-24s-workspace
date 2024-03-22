"""Summing the elements of a list using different loops."""

__author__ = "730653557"


def w_sum(vals: list[float]) -> float:
    """Version A: w_sum - function using a while loop."""
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float: 
    """Version B: f_sum - function using a for... in... loop."""
    sum: float = 0
    for numbers in vals:
        sum += numbers
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Version C: r_range_sum - function using a for... in range(0, len(xs))."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum