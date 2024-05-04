start = 4
n_letters = 1
merr = "@"
for i in range(start, -1, -1):
    print(" " * i, merr * n_letters)
    n_letters = n_letters + 2
