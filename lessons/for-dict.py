"""Practice with Dictionaries and for loops."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

# print out the keys that have True values

for keys in in_stock:
    if in_stock[keys] is True:
        print(keys)
