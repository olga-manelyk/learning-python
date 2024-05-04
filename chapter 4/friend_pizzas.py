my_foods = ["hawaii", "mascarpone", "pancetta"]
friend_pizzas = my_foods[:]

# Додавання нової піцци на початок списку
friend_pizzas.insert(0, "pizzasfish")
my_foods.insert(0, "the Devil pizza")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_pizzas)
