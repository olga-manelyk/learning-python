def sandwiches(*toppings):

    print("\nMaking a sandwiches with the following toppings:")
    for topping in toppings:
        print("- " + topping)


sandwiches("pepperoni")
sandwiches("mushrooms", "green peppers", "extra cheese")
