prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\Enter 'guit' to end the program."
message = " "
while message != "guit":
    message = input(prompt)
    if message != "guit":
        print(message)
