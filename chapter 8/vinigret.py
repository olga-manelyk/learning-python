ingridients2prosesing = {
    "potato": ["boil", "peel", "cut"],
    "cheese": ["grate"],
    "onion": ["peel", "cut"],
    "oil": ["pour"],
}
ingridients = []
while True:
    ingridient = input("what will we prepare the salad from? : ")
    if ingridient == "q":
        break
    if ingridient not in ingridients2prosesing:
        print(f"Sorry, we don't have {ingridient}")
    else:
        ingridients.append(ingridient)


coma_separated_ingridients = ", ".join(ingridients)
print(f"Please make salad from {coma_separated_ingridients}")
for ingridient in ingridients:
    for process in ingridients2prosesing[ingridient]:
        print(f"{process} {ingridient}")
