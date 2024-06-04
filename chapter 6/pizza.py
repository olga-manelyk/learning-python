pizza = {
    "crust": "thich",
    "toppings": ["mushrooms", "exstra chesse"],
}
print(
    "You ordered a "
    + pizza["crust"]
    + " -crust pizza"
    + " with the following toppings:"
)
for toppings in pizza["toppings"]:
    print("\t" + toppings)
