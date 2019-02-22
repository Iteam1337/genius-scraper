import lyricsgenius
from src.to_file import set_content
from src.config import config


genius = lyricsgenius.Genius(config.access_token)
genius.verbose = config.verbose
genius.skip_non_songs = True
genius.remove_section_headers = True
genius.excluded_terms = ["(Remix)", "(Live)"]


def search(artist):
    results = genius.search_artist(
        artist,
        max_songs=config.max_songs,
        sort="title",
    )

    for song in results.songs:
        file_path = "{}/{}/{}/{}.txt".format(
            config.save_path,
            song.artist,
            song.album,
            song.title,
        )
        set_content(file_path, contents=song.lyrics)

    return True
