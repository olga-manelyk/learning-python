# cubes = [f"cube of number: {value} = {value**3} " for value in range(1, 11)]
# print(cubes)
candies = ["mars", "bounty", "twix", "snickers"]
# for candy in candies:
#     print(f"Do you want to eat candy? I have {candy}.")
questions = [f"Do you want to eat candy? I have {candy}." for candy in candies]
print(questions)
