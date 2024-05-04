start = 6
n_letters = 1
merr = "@"
print(" " * (start + 1), merr, sep="")

for i in range(start, -1, -1):
    print(" " * i, merr, " " * n_letters, merr, sep="")
    n_letters = n_letters + 2

print(merr * start * 2)
