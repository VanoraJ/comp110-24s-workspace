"""Functions that implement sorting algorithms."""

__author__ = "730653557"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    length: int = len(x)   # Counter variable to track the indices of the list
    # Overarching loop to iterate through the list
    for index in range(1, length):   # Start from 1 since first element is already sorted
        current_value: int = x[index]
        current_position: int = index

        # Moveing backwards to compare the current element to all elements in the sorted part
        # Check if the unsorted index is greater than zero and the current element is less than the one directly before it.
        while current_position > 0 and x[current_position - 1] > current_value:
            # Swap the 2 elements
            x[current_position] = x[current_position - 1]
            current_position -= 1   # Decrement the unsorted index variable

        # Insert the current element into its correct position within the sorted portion of the list.
        x[current_position] = current_value
 
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    length: int = len(x)   # Counter variable to track the indices of the list
    for outer_index in range(0, length):   # Overarching loop keeping in track of outer index
        # Finding the index of the minimum element in the unsorted protion 
        min_index = outer_index   # Initial minimum index is the current counter value (outer index)

        # Use another loop to find the minimum element in unsorted
        for inner_index in range(outer_index + 1, length):
            if x[inner_index] < x[min_index]:
                min_index = inner_index   # Update the min_index with the new minimum element index
        
        if min_index != outer_index:   # Compare the minimum index to the current outer index
            temporary: int = x[outer_index]
            x[outer_index] = x[min_index]
            x[min_index] = temporary

    return None
    