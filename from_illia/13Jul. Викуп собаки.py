dog = input("Жив пес ")
p_s = f"одного ясного дня  {dog} \n викрали.\n"


day_1 = f"Одного дня {dog} зник ? Його вкрали ?(так/ні/не зовсім/).\n"
day_2 = f"злочинці вимагали за  {dog}  викуп ?(так/ні).\n"
day_3 = f"злочинці вимагали за  {dog}  викуп ?(так/ні/не зовсім/).\n"

ohydni_zapax = (
    f" {dog} був знайдений поліцією.Поліція почала пошук злочинців?\n (так/ні/.\n"
)


print(p_s)
answer = input(day_1)
if answer == "так":
    answer = input("собака був викрадений злочинцями?")
    answer = input(day_2)
    if answer == "так":
        answer = input("1000$?")
    elif answer == "ні":
        print("нічого не просили")


if answer == "ні":
    print(ohydni_zapax)    
elif answer == "ні":
    answer = input("злочинці не знайдені")
else :
    answer == "так":
    answer = input("Злочинці знайдені")


if answer == "не зовсім":
    print(" Так{dog} був на туриторії двору ")
