while True:

    working = input("Вам допомогти ? (так / ні) ")

    if working == "так":
        print("що конкретно Ви шукаєте? )")
        laptop = input(
            " Для яких цілей Вам потрібен ноутбук (Ігровий, для роботи, Для кіно)"
        )
        if laptop == "ігровий":
            print(" Super puper дорогий ноутбук")
        elif laptop == "для роботи":
            print(" Будь який що давно лежить")
        else:
            print("Lenovo 17 super")

    elif working == "ні":
        print("Ідемо за стійку і більше не набридаємо йому")

    print(" Гарного Вам дня !!!")
