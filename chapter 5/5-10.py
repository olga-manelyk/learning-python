current_users = ["olga", "anna", "viktor", "denus", "pavlo", "admin", "ivan"]
new_users = ["anna", "viktor", "denus", "pavlo", "ivan"]

for new_users in current_users:
    if new_users in current_users:
        print("Sorry, username " + new_users + " is not available!")
    else:
        print("Adding " + new_users + ".")

print("\nThank you, colleagues!")
