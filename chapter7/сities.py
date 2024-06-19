prompt = "\nPlease enter the name of a citu you have visited:"
prompt += "\Enter 'guit' when you are finished."
while True:
    citu = input(prompt)
    if citu == "guit":
        break
    else:
        print(" I'd love to do " + citu.title() + "!")
