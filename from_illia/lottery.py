from random import shuffle
from copy import copy

numbers = list(range(1, 76))


# правила нашої лотереї
# 1. 1-75  к-сть кульок в барабані
# 2. 5*15 розмір квитка
# 3. гра ведеться до першого виграшного квитка
# 4. тираж лотереї 1000
# Викидання кульок в довільному порядку
# друк квитків з числами в довільному порядку
# на кожну кульку пошук виграшного квитка
# умова перемоги 3 ряда


GREETING = "Привіт Учасники гри Лото забава"
END_WORD = "кінець"
NAME_REQUEST = f"Введіть імя участика.({END_WORD} якщо учасників більше немає): "

print(GREETING)
participants = {}

while True:
    name = input(NAME_REQUEST)
    if name == END_WORD:
        break
    shuffle(numbers)
    participants[name] = copy(numbers)


def is_row_winning(row, balls):
    wining_row = True
    for number in row:  # берем число з ряда
        if number not in balls:  # якщо число  не в кульках
            wining_row = False  # виключити лампочку
            break  # припинити цикл
    return wining_row


def strike(text):
    result = ""
    for c in text:
        result = result + c + "\u0336"
    return result


strike("Metro")


#


# for _ in range(50):
#     shuffle(numbers)

#     tickets.append()
# print(tickets)
# ticket=[ 26, 3, 14,
#          53, 42, 19]
# balls = [80, 14, 78, 67, 19]
# ticket = [[80, 14], [1, 67]]
# # for row in ticket:
#     # якщо рядок вийграшний
#     # то друкуємо закреслиний рядок
#     # інакще друкуємо незакреслений рядок
#     print((r, balls))
#     balls = [80, 14, 78, 67, 19]


# print(strike())


# for c in "Helloy":
#     print(c)
