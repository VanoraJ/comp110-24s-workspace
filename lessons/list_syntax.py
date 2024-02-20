"""Demostrate Basic List Syntax"""

# Create an empty list
grocery_list: list[str] = list() # <- constructor
grocery_list: list[str] = [] # <- listeral
print("Empty list: ")
print(grocery_list)

# Add to a list
grocery_list.append("frosted flakes")
grocery_list.append("milk")
grocery_list.append("pizza")
print("After adding things:")
print(grocery_list)

# Create a list with object in it
grocery_list2: list[str] = ["frosted flakes", "milk", "pizza"]
print("Already populated list: ")
print(grocery_list2)
print("Add another thing: ")
grocery_list2.append('whipped cream')
print(grocery_list2)

# Indexing
print("Printing one item: ")
print(grocery_list[2])

# Modifying by index
x: list[str] = ["c", "a", "r", "s"]
x[2] = "t"
print(x)

# Length of list
print(len(grocery_list))

# Remove item from list
print("Removing pizza from grocery list: ")
grocery_list.pop(2)
print(grocery_list)

print(["frosted flakes", "milk", "pizza"][0])

grocery_list.append('milk')
print(grocery_list)

# Function name: display
# Parameter: list[str]
# Return nothing
# Print out the list
print("--Functions--")

def display(my_list: list[str]) -> None:
    return print(my_list)

x = display(grocery_list)
print(x)

def create(string1: str, string2: str) -> list[str]:
    new_list: list[str] = [string1, string2]
    return new_list

x: list[str] = create("cake", "cookie")
print(x)
