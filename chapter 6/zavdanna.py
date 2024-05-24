genre_count = {}
for movie in movies:
    for genre in movie["genres"]:
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
print(genre_count)
