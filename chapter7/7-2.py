restaurant_seating = input("How many people are in your dining group?:")
number = int(restaurant_seating)

if number > 8:
    print("\nThe number" + str(number) + " >8 they will have to wait for a table")
else:
    print("\nThe number " + str(number) + " 12  your table is ready ")
    print("I'm sorry, you'll have to wait for a table.")
