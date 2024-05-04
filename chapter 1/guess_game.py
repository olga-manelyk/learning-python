from random import randint

print("Розпочнемо гру!!")
number = randint(1, 100)
# print("я загадала: "+str(number))

while True:
    guess = int(input("введіть число: "))
    # print("ви ввели: "+str(guess))

    if number < guess:
        print("менше")

    if number > guess:
        print("більше")

    if number == guess:
        print("перемога")
        break
