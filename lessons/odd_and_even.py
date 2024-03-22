def odd_and_even(my_list: list[int]) -> list[int]:
    new_list: list[int] = []
    for index in range(0, len(my_list)):
        if my_list[index] % 2 == 1 and index % 2 == 0:
            new_list.append(my_list[index])
    return new_list

def odd_and_even2(my_list: list[int]) -> list[int]:
    new_list: list[int] = []
    index: int = 0
    while index < len(my_list):
        if my_list[index] % 2 == 1 and index % 2 == 0:
            new_list.append(my_list[index])
        index += 1
    return new_list