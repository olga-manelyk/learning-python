inhridiyent = input("введіть вид інгрідієнта")
offer = f"Найкраще {inhridiyent} \n поєднуються у салаті.\n"


appetizer = f"Салат, який має  {inhridiyent} має \n 2300 порцій ? (так/ні/не зовсім).\n"


ohydni_skladovi = f" {inhridiyent} має неприєиний запах \nта залишилися  в камері складу ресторану LONDON.\n"

fertive_evening = "Гості раділи "
print(offer)
answer = input(appetizer)
if answer == "так":
    answer2 = input(
        "смачно та корисно 1000 порцій свіжого салату з морепродуктів Вам ?"
    )
    if int(answer2) > 1000:
        print("замовлення супер ")
    if int(answer2) < 1000:
        print("найсмачкіше в  Україні))")
    print(fertive_evening)
elif answer == "ні":
    print(ohydni_skladovi)
elif answer == "не зовсім":
    print("шукайте нового постачальника")
else:
    print("Не має більше пропозицій")
