def build_profile(first, last, **user_info):

    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "Olha",
    "Maneliuk",
    location="Ostrog",
    native_language="Ukrainian",
    age="35",
    favorite_color=" purple",
)
print(user_profile)
