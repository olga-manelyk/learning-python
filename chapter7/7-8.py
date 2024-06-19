sandwich_orders = [
    "bacon",
    "salami",
    "double cheese",
]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe most delicious sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
