"""Functions that either mutate a function or don't."""


def remove_first(input_list: list[str]) -> None:
    """Remove first element of the list."""
    input_list.pop(0)


def get_first(input_list: list[str]) -> str:
    """Return the first element of the list without mutating."""
    return input_list[0]


def get_and_remove_first(input_list: list[str]) -> str:
    """Removes the first element of the input list and returns it."""
    elem: str = input_list[0]
    input_list.pop(0)
    return elem