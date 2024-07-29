def make_album(performer_name, album_name, amount_tracks=None):
    album = {
        "performer": performer_name,
        "album": album_name,
    }
    if amount_tracks is not None:
        album["number of songs"] = amount_tracks
    return album


while True:
    performer_name = input("Performer name : ")
    if performer_name == "q":
        break

    album_name = input("Album name : ")
    if album_name == "q":
        break

    album = make_album(performer_name, album_name)

    print(album)
