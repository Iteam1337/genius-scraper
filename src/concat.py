import re

from src.file import set_path, traverse, read_content, write_content


def save_all_as_one_file(file_path):
    lines = []

    normalized = set_path(file_path)
    for file in traverse(normalized):
        contents = read_content(file)

        contents = re.sub(r"\n\s*\n", "\n", contents, re.MULTILINE)

        for string in contents.splitlines():
            string = string.strip()
            string = re.sub(r"^\((.*)\)", r"\1", string)
            string = re.sub(r"\.\.\.", "", string)
            string = re.sub(r"([a-zA-ZåäöÅÄÖ)])$", r"\1.", string)
            lines.append(string)

    file_path = "{}.txt".format(normalized)
    write_content(file_path, "\n".join(lines))

    print("wrote file {}".format(file_path))
