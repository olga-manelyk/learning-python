for value in range(1, 100):
    print(value)
    if value % 3:
        print(f"{value} Fizz")

    elif value % 5:
        print(f"{value} Bazz")

        if value % 3 and value % 5:
            print(f"{value} Fizz Bazz")
