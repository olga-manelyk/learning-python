for value in range(1, 100):
    if value % 3 == 0 and value % 5 == 0:
        print("FizzBazz")

    elif value % 5 == 0:
        print("Bazz")

    elif value % 3 == 0:
        print("Fizz")
    else:
        print(value)
