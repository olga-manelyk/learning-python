while True:

    казка = input("Вітаю дітки давайте поряхуємо слоненят? ( так/ ні) ? ")
    name = input("введіть імя МАМИ  слоненят ")

    if казка == "так":
        print(f"жили на світі 3 слоненяток, діток мами {name}  Дінні  -Кікі і Дуся! )")
        pep = input(
            " якось слоненятка пішли на прогулянку до річки  і вони побачили (печеру , яму , ліс)"
        )
        if pep == "печеру":
            print(" вона була глибока, і люди боялися туди заходити")
        elif pep == "яму":
            print(" глибоку")
        else:
            print(" страшні хащі")

    elif казка == "ні":
        print(" на сьогодні ми втомитися")

    number = input(" введіть яку к-сть слоненяток  оголошено в казці:")
    number = int(number)
    if number == 3:
        print(
            "\n   вітаю "
            + str(number)
            + " ви уважні  чекаю Вас знову до країни казок!!!"
        )
    else:
        print(
            "\n  думайте краще  дітки !!!"
            + str(number)
            + " ні, вибачте  відповідь не вірна ..."
        )
    print(
        f"Ввечері слоненяткa  і їх мама {name} розповідали \nпро день,проведений у стайні, таткові."
    )
    print(f"чекаємо Вас знову  в нашому світі казкових пригод, сказала мама {name}!!!.")
