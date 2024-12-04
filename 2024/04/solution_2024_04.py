from pathlib import Path

SEARCH_X_POSITIVE_DIRECTION = 1
SEARCH_X_NEGATIVE_DIRECTION = -1
DO_NOT_SEARCH_IN_X_DIRECTION = 0
SEARCH_Y_POSITIVE_DIRECTION = 1
SEARCH_Y_NEGATIVE_DIRECTION = -1
DO_NOT_SEARCH_IN_Y_DIRECTION = 0

SEARCH_RIGHT = SEARCH_X_POSITIVE_DIRECTION, DO_NOT_SEARCH_IN_Y_DIRECTION
SEARCH_LEFT = SEARCH_X_NEGATIVE_DIRECTION, DO_NOT_SEARCH_IN_Y_DIRECTION
SEARCH_DOWN = DO_NOT_SEARCH_IN_X_DIRECTION, SEARCH_Y_POSITIVE_DIRECTION
SEARCH_UP = DO_NOT_SEARCH_IN_X_DIRECTION, SEARCH_Y_NEGATIVE_DIRECTION
SEARCH_DOWN_AND_RIGHT = SEARCH_X_POSITIVE_DIRECTION, SEARCH_Y_POSITIVE_DIRECTION
SEARCH_DOWN_AND_LEFT = SEARCH_X_NEGATIVE_DIRECTION, SEARCH_Y_POSITIVE_DIRECTION
SEARCH_UP_AND_RIGHT = SEARCH_X_POSITIVE_DIRECTION, SEARCH_Y_NEGATIVE_DIRECTION
SEARCH_UP_AND_LEFT = SEARCH_X_NEGATIVE_DIRECTION, SEARCH_Y_NEGATIVE_DIRECTION

SEARCH_DIRECTIONS = (
    SEARCH_RIGHT,
    SEARCH_LEFT,
    SEARCH_DOWN,
    SEARCH_UP,
    SEARCH_DOWN_AND_RIGHT,
    SEARCH_DOWN_AND_LEFT,
    SEARCH_UP_AND_RIGHT,
    SEARCH_UP_AND_LEFT,
)


def is_word_found_for_position_and_direction(
    word_search: list[str],
    word: str,
    line_number: int,
    character_position: int,
    direction: tuple[int, int],
) -> bool:
    """Confirm if a word is found at the given position in the given direction.

    Args:
        word_search (list[str]): The puzzle to search in
        word (str): The word to find the occurrences for
        line_number (int): The line number to start searching from
        character_position (int): The character in the line to start searching from
        direction (tuple[int, int]): The direction to search in

    Returns:
        bool: True if the word can be found
    """

    def get_word_at_position_and_direction() -> str:
        number_of_lines = len(word_search)
        length_of_lines = len(word_search[0]) if number_of_lines > 0 else 0

        found_word: list[str] = []
        current_line_number = line_number
        current_character_position = character_position

        while (
            0 <= current_line_number < number_of_lines
            and 0 <= current_character_position < length_of_lines
            and len(found_word) < len(word)
        ):
            found_word.append(
                word_search[current_line_number][current_character_position]
            )
            current_line_number += direction[1]
            current_character_position += direction[0]

        return "".join(found_word)

    word_at_position_and_direction = get_word_at_position_and_direction()

    return word == word_at_position_and_direction


def count_number_of_occurrences_at_position(
    word_search: list[str], word: str, line_number: int, character_position: int
) -> int:
    """Confirm if word is found at given position.

    Args:
        word_search (list[str]): The puzzle to search in
        word (str): The word to find the occurrences for
        line_number (int): The line number to start searching from
        character_position (int): The character in the line to start searching from

    Returns:
        int: The number of occurrences at the given position
    """
    number_of_occurrences = 0

    for direction in SEARCH_DIRECTIONS:
        if is_word_found_for_position_and_direction(
            word_search, word, line_number, character_position, direction
        ):
            number_of_occurrences += 1

    return number_of_occurrences


def count_number_of_occurrences(word_search: list[str], word: str) -> int:
    """Count the number of word occurrences in a word search puzzle.

    Args:
        word_search (list[str]): The puzzle to search in
        word (str): The word to find the occurrences for

    Returns:
        int: The number of occurrences of the word
    """
    total_occurrences = 0
    number_of_lines = len(word_search)
    length_of_lines = len(word_search[0]) if number_of_lines > 0 else 0

    for line_number in range(number_of_lines):
        for character_position in range(length_of_lines):
            if word_search[line_number][character_position] != word[0]:
                continue

            number_of_occurrences_at_position = count_number_of_occurrences_at_position(
                word_search, word, line_number, character_position
            )
            total_occurrences += number_of_occurrences_at_position

    return total_occurrences


def get_input(file_path: str) -> list[str]:
    """Read the word search puzzle from file.

    Args:
        file_path (str): The file path for the word search

    Returns:
        list[str]: The list if lines from the word search
    """
    with Path(file_path).open() as file:
        all_lines = file.readlines()
        return [line.rstrip("\n") for line in all_lines]


def main() -> None:
    """Main entry point for the application."""
    word_search = get_input("/workspaces/advent-of-code/2024/04/input.txt")

    number_of_occurrences = count_number_of_occurrences(word_search, "XMAS")
    print(f"Number of XMAS occurrences = {number_of_occurrences}")


if __name__ == "__main__":
    main()
