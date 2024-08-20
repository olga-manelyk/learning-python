# 1.movement direction
# 2. DONE how to store snake
# 3. DONE how to draw snake
#


from time import sleep

import curses

snake = [
    [8, 2],
    [7, 2],
    [6, 2],
    [5, 2],
    [5, 3],
    [5, 4],
]


def draw_snake(screen):
    for coordinate in snake:
        # screen.clear()  # oчищвє екран

        screen.addch(
            coordinate[0], coordinate[1], "n"
        )  # ставить символ за координатами друкує n


def move_snake(x, y, direction):
    if direction == "left":  # вліво
        y -= 1
    if direction == "right":  # вправо
        y += 1
    if direction == "down":  # вниз
        x -= 1
    if direction == "up":  # вгору
        x += 1
    return x, y


def main(screen):  # приймаємо екран і  викл wrapper
    curses.curs_set(0)  # робим не видимим курсор
    while snake:
        draw_snake(screen)  # вик. функцію "намалюй змію" по точках  проходиться
        screen.refresh()  # оновлюємо екран
        sleep(1)  # (час)
        screen.clear()  # oчистити
        snake.pop(0)  # видадяє хвіст зі списку  останній елемент
        snake.append(
            move_snake(
                snake[-1][
                    0
                ],  # від голови перша координата на першому кроці 5,5   5,4  5,4 5,3 ....[0]-5
                snake[-1][1],  # 5,4
                "right",
            )
        )


curses.wrapper(
    main
)  # ініціалізую  curses  викликає main і завершує роботу з бібліотекою
