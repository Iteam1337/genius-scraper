from argparse import ArgumentParser
from src.genius import search


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-a', '--artist')
    args = parser.parse_args()

    search(args.artist)
