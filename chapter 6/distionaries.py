alien_0 = {"x_positions": 0, "y_positions": 25, "speed": "medium"}
print("Original x-position: " + str(alien_0["x_positions"]))
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0["x_positions"] = alien_0["x_positions"] + x_increment

print("New x_position: " + str(alien_0["x_positions"]))
