prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\Enter 'guit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == "guit":
        active = False
    else:
        print(message)
