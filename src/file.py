from os import path, makedirs, walk

from src.config import config


def set_path(file_path):
    return path.normpath("{}/{}".format(config.save_path, file_path))


def read_content(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def write_content(file_path, content):
    f = None
    try:
        f = open(file_path, "w")
        f.write(content)
        f.close()
    except Exception as e:
        print(e)
        pass
    finally:
        if f:
            f.close()


def set_content(file_path, content):
    normalized = set_path(file_path)

    dir_path = path.dirname(normalized)

    try:
        makedirs(dir_path, exist_ok=True)
    except FileExistsError:
        pass

    write_content(normalized, content)


def traverse(file_path):
    save_files = []

    for root, _dirs, files in walk(file_path):
        if root == file_path:
            continue

        if not files:
            continue

        for file_name in files:
            save_files.append(path.normpath("{}/{}".format(root, file_name)))

    return save_files
