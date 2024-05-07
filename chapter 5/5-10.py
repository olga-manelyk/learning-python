current_users = ["olga", "anna", "viktor", "denus", "pavlo", "admin", "ivan"]
new_users = ["john", "viktor", "denus", "biba", "boba"]

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, username " + new_user + " is not available!")
    else:
        print("Adding " + new_user + ".")

print("\nThank you, colleagues!")
