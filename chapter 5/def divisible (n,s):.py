def divisible(n, s):
    return not n % s


h = 4
if divisible(h, 5):
    print("Bazz")
elif divisible(h, 3):
    print("Fizz")
else:
    print("Hello Olga")
