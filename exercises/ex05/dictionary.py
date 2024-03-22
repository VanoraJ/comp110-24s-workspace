"""EX05 - Dictionary Functions."""

__author__ = "730653557"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Function invert the original dict's key to value, and value to key."""
    inverted_dict: dict[str, str] = {}
    for key in my_dict:
        value: str = my_dict[key]
        if value in inverted_dict:
            raise KeyError(f"Duplicate key found when trying to invert: {value}")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(name_and_coloar: dict[str, str]) -> str:
    """Function returns the color that appears most frequently."""
    count_dict: dict[str, int] = {}
    for name in name_and_coloar:
        color = name_and_coloar[name]
        if color in count_dict:
            count_dict[color] += 1
        else:
            count_dict[color] = 1

    max_count: int = 0
    favorite: str = ""

    for color in count_dict:
        count: int = count_dict[color]

        if count > max_count:
            max_count = count
            favorite = color
    
    return favorite


def count(my_list: list[str]) -> dict[str, int]:
    """Function produce a dictionary that use the provided list's value as key and the dict's value is the number of times such list's value (dict key) appeared in the list."""
    new_dict: dict[str, int] = {}
    for item in my_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1

    return new_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Function produce a dictionary that use each letter in the alphabet as key, and use the provided list's words that begin with the key's letter as value."""
    new_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter: str = word[0].lower()

        if first_letter not in new_dict:
            new_dict[first_letter] = [word]
        else:
            new_dict[first_letter].append(word)

    return new_dict


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    """Function returns a dict that update the original attendance dict with new attendence info."""
    if day in attendance:
        if name not in attendance[day]:
            attendance[day].append(name)
    else:
        attendance[day] = [name]