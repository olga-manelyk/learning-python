def bla_bla(message, options):
    question = f"{message} ({', '.join(options)}): "
    while True:
        option = input(question).strip().lower()
        if option in options:
            break
    return option


bla_bla("введіть", {"так", "ні"})
print("Hello")
bla_bla("введіть велике число", {"ліси", "дуби", "пір'я"})
