def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(12, "pepperoni", "mushrooms", "extra cheese")
make_pizza(16, "sausage", "green peppers", "onions", "olives")
