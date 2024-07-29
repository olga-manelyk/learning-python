def show_megicians(magicians):
    """Print all messages in the list."""
    for magician in magicians:
        magician = "Великий " + magician.title() + "!"
        print(magician)


magicians = [
    "Lyka",
    "Pedro",
]
show_megicians(magicians)
