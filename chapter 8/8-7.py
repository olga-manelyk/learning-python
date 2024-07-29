def make_album(performer_name, album_name, amount_tracks=None):
    album = {
        "performer": performer_name,
        "album": album_name,
    }
    if amount_tracks is not None:
        album["number of songs"] = amount_tracks
    return album


musician = make_album(
    "Michael Jackson",
    "Got to Be There",
)
print(musician)
