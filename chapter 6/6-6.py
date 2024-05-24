favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
# for name, language in favorite_languages.items():
#     print(name.title() + " 'favorite language is " + language.title() + ".")

friends = ["phil", "sarah", "anton"]
for name in friends:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for taking my poll")
    else:
        print(f"Please {name.title()} take my poll")
