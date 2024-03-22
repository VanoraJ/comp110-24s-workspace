"""EX06 - Unit Test for EX05."""

__author__ = "730653557"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

# Part 1 - invert function test


def test_invert_empty() -> None:
    """Use test - function with empty dict input should return an empty dict."""
    assert invert({}) == {}


def test_invert_basic() -> None:
    """Use test - test the basic function to see if return inverted dict."""
    input_dict: dict[str, str] = {"big": "small", "high": "low", "tall": "short"}
    assert invert(input_dict) == {"small": "big", "low": "high", "short": "tall"}


def test_invert_unusual() -> None:
    """Edge test - test if function works on some unusual input strings."""
    input_dict: dict[str, str] = {"~": "!", "1": "2", "&": "@"}
    assert invert(input_dict) == {"!": "~", "2": "1", "@": "&"}


# Part 2 - favorite_color test


def test_fc_basic() -> None:
    """Use test - basic function of returning the most appeared color."""
    input_dict: dict[str, str] = {"Mark": "blue", "James": "yellow", "Anna": "yellow", "Lily": "red"}
    assert favorite_color(input_dict) == "yellow"


def test_fc_tie() -> None:
    """Use test - return the first appeared tie color if tied."""
    input_dict: dict[str, str] = {"Mark": "red", "James": "yellow", "Anna": "yellow", "Lily": "red"}
    assert favorite_color(input_dict) == "red"


def test_fc_single() -> None:
    """Edge test - return the input color if only 1 color is inputed."""
    input_dict: dict[str, str] = {"Mark": "red"}
    assert favorite_color(input_dict) == "red"


# Part 3 - count test
    

def test_count_basic() -> None:
    """Use test - produce a dict that keeps tract of the number of appearance of each element in input list."""
    input_list: list[str] = ["cat", "dog", "rabbit", "cat", "goldfish"]
    assert count(input_list) == {"cat": 2, "dog": 1, "rabbit": 1, "goldfish": 1}


def test_count_unique() -> None:
    """Use test - testing a list that have all its elements different."""
    input_list: list[str] = ["cat", "dog", "rabbit", "bird", "goldfish"]
    assert count(input_list) == {"cat": 1, "dog": 1, "rabbit": 1, "bird": 1, "goldfish": 1}
 

def test_count_empty() -> None:
    """Edge test - testing using an empty list, should return an empty dict."""
    input_list: list[str] = []
    assert count(input_list) == {}


# Part 4 - alphabetizer test
    

def test_alphabetizer_basic() -> None:
    """Use test - basic function of returning dict that have its key as first letter and value as the words starting with key's letter."""
    input_list: list[str] = ["dream", "sleep", "pillow", "sugar", "candy", "cat", "dog"]
    assert alphabetizer(input_list) == {"d": ["dream", "dog"], "s": ["sleep", "sugar"], "p": ["pillow"], "c": ["candy", "cat"]}


def test_alphabetizer_case_difference() -> None:
    """Use test - function should still work normally when the inputted list contains words of different upper or lowercase."""
    input_list: list[str] = ["Dream", "SLEEP", "piLLOW", "sugar", "Candy", "cat", "DOG"]
    assert alphabetizer(input_list) == {"d": ["Dream", "DOG"], "s": ["SLEEP", "sugar"], "p": ["piLLOW"], "c": ["Candy", "cat"]}


def test_alphabetizer_empty() -> None:
    """Edge test - return an empty dict if input list is empty."""
    input_list: list[str] = []
    assert alphabetizer(input_list) == {}


# Part 5 - update_attendance test


def test_ua_existing_day() -> None:
    """Use test - adding a name to an existing date."""
    input_dict: dict[str, list[str]] = {"Monday": ["Lisa", "James"], "Tuesday": ["Alice", "Bill"]}
    expect_dict: dict[str, list[str]] = {"Monday": ["Lisa", "James", "Jack"], "Tuesday": ["Alice", "Bill"]} 
    update_attendance(input_dict, "Monday", "Jack")
    assert input_dict == expect_dict


def test_ua_new_day() -> None:
    """Use test - adding a name to a new date while also adding a name to an existing date."""
    input_dict: dict[str, list[str]] = {"Monday": ["Lisa", "James"], "Tuesday": ["Alice", "Bill"]}
    update_attendance(input_dict, "Monday", "Jack")
    update_attendance(input_dict, "Wednesday", "Lisa")
    expect_dict: dict[str, list[str]] = {"Monday": ["Lisa", "James", "Jack"], "Tuesday": ["Alice", "Bill"], "Wednesday": ["Lisa"]}
    assert input_dict == expect_dict


def test_ua_empty_name() -> None:
    """Edge test - function returns an empty list for the day that no name was inputted."""
    input_dict: dict[str, list[str]] = {"Monday": ["Lisa", "James"], "Tuesday": ["Alice", "Bill"]}
    update_attendance(input_dict, "Wednesday", "")
    expect_dict: dict[str, list[str]] = {"Monday": ["Lisa", "James"], "Tuesday": ["Alice", "Bill"], "Wednesday": [""]}
    assert input_dict == expect_dict