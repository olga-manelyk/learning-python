cities = {
    "Ukraine": "egypt",
    "Italli: "ukraine",
    "Greece": "greece",
    "Turkey": "turkey",
}
for name, river in rivers_favorite.items():
    print(name.title() + " flows through " + river.title() + ".")


for name in rivers_favorite.keys():
    print(name.title())


for river in rivers_favorite.values():
    print(river.title())
