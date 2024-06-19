# скільки сімей ми можемо розмістити в театрі в 1 ряду
# потрібно дізнатися які букви місць зарезервовані  в конкретному ряду
# BCDE,   DEFG, FGHJ.
# E   FGHJ
# A BCDE, FGHJ,
# CDEFGHJK
def get_row2sits(tikets):
    row2sits = {}
    for tiket in tikets.split():
        row = int(tiket[:-1])
        sit = tiket[-1]
        if row in row2sits:
            row2sits[row].add(sit)
        else:
            row2sits[row] = {sit}
    return row2sits


def amount_of_families(tikets, n_rows):
    row2sits = get_row2sits(tikets)
    families = 0
    all_sits = set("ABCDEFGHJK")

    for row in range(1, n_rows + 1):
        occupied = row2sits.get(row, set())
        empty_seats = all_sits - occupied
        if set("BCDEFGHJ").issubset(empty_seats):
            families = families + 3
        elif set("DEFG").issubset(empty_seats):
            families = families + 1
        elif set("FGHJ").issubset(empty_seats):
            families = families + 1
        elif set("BCDE").issubset(empty_seats):
            families = families + 1
    return families


"1A 2B 3C 4D 5E 6F 7G 8H 9J 10K"


empty_seats = "ABCDEFGHJK"
