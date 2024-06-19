number = input("Enter a number, and I will say whether it is divisible by :")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " yes, the number is divisible")
else:
    print("\nThe number " + str(number) + " no, the number is not divisible ")
