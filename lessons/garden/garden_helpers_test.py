"""Test my garden functions."""

__author__ = "730653557"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

# Part 1 - Unit test for add_by_kind


def test_add_by_kind_existing_kind() -> None:
    """Use case - adding a plant to an existing plant type."""
    plants: dict[str, list[str]] = {"flower": ["sunflower", "tulip"]}
    add_by_kind(plants, "flower", "daisy")
    result: dict[str, list[str]] = {"flower": ["sunflower", "tulip", "daisy"]}
    assert plants == result


def test_add_by_kind_initial_empty() -> None:
    """Edge case - adding a plant to an initially empty input dictionary."""
    plants: dict[str, list[str]] = {}
    add_by_kind(plants, "flower", "daisy") 
    result: dict[str, list[str]] = {"flower": ["daisy"]}
    assert plants == result


# Part 2 - Unit test for add_by_date


def test_add_by_date_new_month() -> None:
    """Use case - adding a plant to a new month."""
    plants: dict[str, list[str]] = {"March": ["lily"], "April": ["sunflower", "tulip"]}
    add_by_date(plants, "June", "rose")
    result: dict[str, list[str]] = {"March": ["lily"], "April": ["sunflower", "tulip"], "June": ["rose"]}
    assert plants == result 


def test_add_by_date_empty_input() -> None:
    """Edge case - to simulate accidentally adding an empty entry of plant."""
    plants: dict[str, list[str]] = {"March": ["lily"], "April": ["sunflower", "tulip"]}
    add_by_date(plants, "June", "")
    result: dict[str, list[str]] = {"March": ["lily"], "April": ["sunflower", "tulip"], "June": [""]}
    assert plants == result 

 
# Part 3 - Unit test for lookup_by_kind_and_date


def test_lookup_by_kind_and_date_basic_search() -> None:
    """Use case - basic functionality simulation - e.g. flower in March."""
    plant_by_kind: dict[str, list[str]] = {"flower": ["rose", "daisy", "sunflower"], "vegetable": ["tomato", "onion", "potato"]}
    plant_by_date: dict[str, list[str]] = {"March": ["rose", "tomato"], "June": ["daisy", "sunflower"], "July": ["onion", "potato"]}
    expected = "flower to plant in March: ['rose']"
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, "flower", "March")
    assert expected == result


def test_lookup_by_kind_and_date_no_overlap() -> None:
    """Edge case - no overlap between the 2 dictionaries - e.g. vegetable in Jume."""
    plant_by_kind: dict[str, list[str]] = {"flower": ["rose", "daisy", "sunflower"], "vegetable": ["tomato", "onion", "potato"]}
    plant_by_date: dict[str, list[str]] = {"March": ["rose", "tomato"], "June": ["daisy", "sunflower"], "July": ["onion", "potato"]} 
    expected = "No vegetable to plant in June"
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, "vegetable", "June")
    assert expected == result 