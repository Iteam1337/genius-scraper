from os import path, makedirs


def set_content(file_path, contents):
    norimalized = path.normpath(file_path)
    dir_path = path.dirname(norimalized)

    try:
        makedirs(dir_path, exist_ok=True)
    except FileExistsError:
        pass

    f = None
    try:
        f = open(norimalized, 'w')
        f.write(contents)
        f.close()
    except Exception as e:
        print(e)
        pass
    finally:
        if f:
            f.close()
