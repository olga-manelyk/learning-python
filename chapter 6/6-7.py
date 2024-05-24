people = [
    {"name": "anna", "surname": "smirnova", "age": "5", "city": "ostrog"},
    {"name": "denus", "surname": "smirnova", "age": "5", "city": "italy"},
    {"name": "elena", "surname": "smirnova", "age": "38", "city": "turkey"},
]
for human in people:
    print(
        f"name-{human['name'].title()} "
        f"surname-{human['surname'].title()} "
        f"age-{human['age']} "
    )
