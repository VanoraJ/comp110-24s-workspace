"""Practice instantiating Pizza Class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
sals_pizza: Pizza = Pizza("small", 2, False)


# def price(pizaa_order: Pizza) -> float:
#     """Calculate and return cost of pizza."""
#     cost: float = 0.0
#     if pizaa_order.size == "large":
#         cost += 6.0
#     else:
#         cost += 5.0
#     # charge 0.75 per topping
#     cost += 0.75 * pizaa_order.toppings
#     # charge 1 for gluten free
#     if pizaa_order.gluten_free == True:
#         cost += 1.0
#     return cost

print(my_pizza.toppings)
print((my_pizza.price()))

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print((my_pizza.price()))