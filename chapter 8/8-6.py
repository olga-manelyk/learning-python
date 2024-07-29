def city_country(city, country):
    return f"{city.title()}, {country.title()}"


city = city_country("santiago", "chile")
print(city)

city = city_country("ukraine", "ostrog")
print(city)

city = city_country("italy ", "Orvieto")
print(city)
