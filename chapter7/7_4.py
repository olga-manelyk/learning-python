pizza_toppings = "\nPlease enter a range of pizza toppings:"
pizza_toppings += "\nEnter 'quit' when you are finished."

while True:
    topping = input(pizza_toppings)
    if topping.lower() == "quit":
        break
    else:
        print("You added this topping to your pizza: " + topping.title() + "!")
