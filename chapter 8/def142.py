def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + "  " + middle_name + last_name
    return full_name.title()


musician = get_formatted_name("johh", "lee ", "hooker")
print(musician)
