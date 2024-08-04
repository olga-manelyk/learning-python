def show_megicians(magicians):

    for magician in magicians:
        magician = "Великий " + magician.title() + "!"
        print(magician)


magicians = [
    "Lyka",
    "Pedro",
]
show_megicians(magicians)
