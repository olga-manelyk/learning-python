def make_shirt(shirt_size, message_s):
    print("\nShirt size: " + shirt_size + ".")
    print("Message: " + message_s + ".")


make_shirt("M", "I love cheese")
make_shirt(message_s="big guy", shirt_size="xxl")
d = {"message_s": "small girl", "shirt_size": "m"}
make_shirt(**d)
l = ["x", "python programmer"]
make_shirt(*l)
