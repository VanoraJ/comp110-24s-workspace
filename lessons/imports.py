"""The file where I import stuff."""

from lessons import my_functions #This also runs the my_functions module, thereby it prints out 3 as well
# or use from lessons.my_functions import add, my_variable

# __name__ = "__main__" Therefore, only this module will be ran
print(my_functions.add(4, 5))

print(my_functions.my_variable)