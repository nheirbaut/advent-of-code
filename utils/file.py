from pathlib import Path


def read_all_lines_from_file(file_path: str) -> list[str]:
    """Read al lines from a given file.

    All lines will be stripped from trailing whitespace.

    Args:
        file_path (str): The file to read the lines from

    Returns:
        list[str]: The lines from the file
    """
    with Path(file_path).open() as file:
        return [line.rstrip() for line in file]
