def hash_browns(people, **filling):
    print(f"натерти {300*people} г картоплі")
    print(f"додати {1*people} яєць")
    print(f"{2*people} cт.л борошна")
    print(f"перемішати +{filling} і посмажити ")


hash_browns(
    people=4, filling=["гриби", "мясо", "cир"], oil="olive", way="запекти в духовці"
)
