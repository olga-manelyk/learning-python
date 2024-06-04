# Написати функцію, яка отримує на вхід стрічку зі стрілочками виду "^^<<>><><^"
# Потрібно знайти мінімальну кількість замін стрілочок, щоб вони всі дивились в одну сторону


# 1. порахувати стрілочки кожного виду
{"^": 3, ">": 3, "<": 4}
# 2. знайти найбільшу к-сть стрілочок 1 виду
# 3.


example = "^^<<>><><^"
expected = {"^": 3, ">": 3, "<": 4}


def find_minimal_amount_of_substution(arrows):
    result = {}
    for arrow in arrows:
        if arrow in result:
            result[arrow] = result[arrow] + 1
        else:
            result[arrow] = 1
    return len(arrows) - max(result.values())
