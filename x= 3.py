x = 3
for value in range(1, 100):
    if value % 3 == 0:
        print("Bazz")
    if value % 3 == 0 and value % x == 0:
        print("FizzBazz")
