"""Challenge Question 07 - Recursive Function."""

__author__ = "730653557"


def f(n: int, k: int) -> int:
    """Recursive Form."""
    if n == 0: 
        return 0
    else: 
        return f(n - 1, k) + k