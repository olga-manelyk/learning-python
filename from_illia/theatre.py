# скільки сімей ми можемо розмістити в театрі в 1 ряду
# потрібно дізнатися які букви місць зарезервовані  в конкретному ряду
# BCDE,   DEFG, FGHJ.
# E   FGHJ
# A BCDE, FGHJ,
# CDEFGHJK

empty_seats = "ABCDEFGHJK"
if "BCDEFGHJ" in empty_seats:
    print(2)
elif "DEFG" in empty_seats:
    print(1)
elif "FGHJ" in empty_seats:
    print(1)
elif "BCDE" in empty_seats:
    print(1)
else:
    print(0)

"1A 2B 3C 4D 5E 6F 7G 8H 9J 10K"

empty_seats = "ABCDEFGHJK"
