import lyricsgenius
from src.file import set_content
from src.concat import save_all_as_one_file
from src.config import config


genius = lyricsgenius.Genius(config.access_token)
genius.verbose = config.verbose
genius.skip_non_songs = True
genius.remove_section_headers = True
genius.excluded_terms = [
    "(Remix)",
    "(Live)",
    "(Akustisk)",
    "(Instrumental)",
    "(Radio Edit)",
    "(Singelversion)",
    "(Filtenmix)",
    "(Interlude)",
    "(Freestyle)",
    "(Grammys)",
    "(Outro)",
    "(Intro)",
    "(Music Video)",
    "(Clean)",
]


def search(artist):
    artists = set()

    results = genius.search_artist(artist, max_songs=config.max_songs)

    for song in results.songs:
        if not song.album:  # ignore ep/singles
            continue

        file_path = "{}/{}/{}.txt".format(song.artist, song.album, song.title)

        set_content(file_path, content=song.lyrics)
        artists.add(song.artist)

    for artist in artists:
        save_all_as_one_file(artist)

    return True
