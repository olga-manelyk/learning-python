favorite_place = {
    "anna": ["mom is happy", "Kindergarten", "pizzeria"],
    "olena": ["zara store", "library", "grocery store"],
    "ivan": ["park", "Lithuania", "film studio"],
}

for name, places in favorite_place.items():
    for place in places:
        print(f"{name.title()} favorite place {place.title()}.")


for name in favorite_place.keys():
    print(name.title())
