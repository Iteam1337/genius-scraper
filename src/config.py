from os import getenv
from types import SimpleNamespace
from dotenv import load_dotenv, find_dotenv

if __name__ != "__main__":
    load_dotenv(find_dotenv(filename=".env"))

    config = {
        "verbose": getenv("VERBOSE", default="").lower() == "true",
        "access_token": getenv("ACCESS_TOKEN", default=""),
        "save_path": getenv("SAVE_PATH", default="out"),
        "max_songs": int(getenv("MAX_SONGS", default="3")),
    }

    config = SimpleNamespace(**config)
