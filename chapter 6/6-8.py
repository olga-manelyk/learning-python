house_pets = []
called_pets = [
    {"name": "bonua", "breed": "rottweiler", "age": "13", "city": "ostrog"},
    {"name": "cat", "breed": "Burmese cat", "age": "4", "city": "italy"},
]

for pet in called_pets:
    name = f"{pet['name'].title()} {pet['breed'].title()}"
    age = pet["age"]
    city = pet["city"].title()

    print(f"{name}, of {city}, is {age} years old.")
