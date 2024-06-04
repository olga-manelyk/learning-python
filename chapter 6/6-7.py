called pets = [
    {"name": "boba", "breed": "rottweiler", "age": "12", "city": "ostrog"},
    {"name": "denus", "surname": "sokil", "age": "88", "city": "italy"},
    {"name": "elena", "surname": "smirnova", "age": "38", "city": "turkey"},
]

for person in people:
    name = f"{person['name'].title()} {person['surname'].title()}"
    age = person["age"]
    city = person["city"].title()

    print(f"{name}, of {city}, is {age} years old.")
