favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(
            " Hi "
            + name.title()
            + ", I see your favorite_languages is "
            + favorite_languages[name].title()
            + "!"
        )
