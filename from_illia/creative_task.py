# # for if else input
# Бот який шукає контакти по підстрічці (substring)
# користувач вводить якусь стрічку, бот друкує всі контакти в яких є така стрічка

places_interest = {
    "Odessa": "port",
    "Kuiv": "dnipro",
    "Lviv": "kavyatria",
    "London": "big ben",
}
print(places_interest)
search_str = input("\n enter a point of interest??")
for name, interest in places_interest.items():
    if interest.upper() in name.upper():
        print(f"{name}--{interest}")
    elif name.upper() in name.upper():
        print(f"{name}")
