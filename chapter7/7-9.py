print("Deli hali run out of pastrami")
sandwich_orders = [
    "bacon",
    "pastrami",
    "salami",
    "pastrami",
    "double cheese",
    "pastrami",
]
finished_sandwiches = []
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    print(sandwich_orders)
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe most delicious sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
