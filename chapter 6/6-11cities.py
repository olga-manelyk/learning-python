cities = {
    "Lviv": {
        "population": 721_000,
        "fact": (
            "Traces of its Polish and Austro-Hungarian heritage are evident in its architecture,"
            " which blends Central and Eastern European styles with those of Italy and Germany"
        ),
        "country": "Ukraine",
    },
    "London": {
        "population": 8_982_000,
        "fact": "The capital of Great Britain",
        "country": "Great Britain",
    },
    "New York": {
        "population": 8_336_000,
        "fact": "Broadway theater is located here",
        "country": "USA",
    },
}
TEMPLATE = """
City: {city_name}
Number of citizens: {population}
Intresting info: {fact}
Country: {country}
"""


# for name, city_info in cities.items():
#     print(
#         TEMPLATE.format(
#             city_name=name,
#             population=city_info["population"],
#             fact=city_info["fact"],
#             country=city_info["country"],
#         )
#     )
for name, city_info in cities.items():
    print(TEMPLATE.format(city_name=name, **city_info))
