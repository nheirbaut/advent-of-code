from pathlib import Path


def create_lab_layout_from_lines(lines: list[str]) -> list[list[str]]:
    """Create a character based lab layout from lines.

    Args:
        lines (list[str]): The lines to create the layout from

    Returns:
        list[list[str]]: The lab layout
    """
    return [list(line) for line in lines]


def get_lab_layout_from_file(file_path: str) -> list[list[str]]:
    """Get the layout of the lab from a file.

    Args:
        file_path (str): The file defining the lab layout

    Returns:
        list[str]: The layout of the lab
    """
    with Path(file_path).open() as file:
        all_lines = file.readlines()
        all_lines = [line.rstrip() for line in all_lines]

        return create_lab_layout_from_lines(all_lines)


def find_start_position(lab_layout: list[list[str]]) -> tuple[int, int]:
    """Find te start position in the lab.

    Args:
        lab_layout (list): The lab layout

    Returns:
        tuple[int, int]: The lin index and character position of the starting point
    """
    for line_index, line in enumerate(lab_layout):
        for char_index, char in enumerate(line):
            if char == "^":
                return line_index, char_index

    return 0, 0


def walk_to_outside_of_lab(lab_layout: list[list[str]]) -> None:
    """Walk to the outside of the lab.

    Args:
        lab_layout (list[list[str]]): The lab layout
    """
    up_delta = (0, -1)
    down_delta = (0, 1)
    left_delta = (-1, 0)
    right_delta = (1, 0)

    possible_directions: list[tuple[int, int]] = [
        up_delta,
        right_delta,
        down_delta,
        left_delta,
    ]

    line_position, char_position = find_start_position(lab_layout)

    current_direction_index = 0
    person_is_outside_the_lab = False

    while not person_is_outside_the_lab:
        next_line_position = (
            line_position + possible_directions[current_direction_index][1]
        )
        next_char_position = (
            char_position + possible_directions[current_direction_index][0]
        )

        # Determine blockage
        if lab_layout[next_line_position][next_char_position] == "#":
            current_direction_index += 1

            if current_direction_index == len(possible_directions):
                current_direction_index = 0

            continue

        # No blockage, move forward
        lab_layout[line_position][char_position] = "X"
        line_position = next_line_position
        char_position = next_char_position

        # See if we moved outside
        if (
            line_position < 0
            or line_position >= len(lab_layout)
            or char_position < 0
            or char_position >= len(lab_layout[0])
        ):
            break


def get_number_of_distinct_moves(lab_layout: list[list[str]]) -> int:
    """Get the number of distinct movements within the lab.

    Args:
        lab_layout (list[list[str]]): The lab layout with movements

    Returns:
        int: The total number of distinct movements
    """
    return sum(line.count("X") for line in lab_layout)


def main() -> None:
    """Main entry point for the application."""
    lab_layout = get_lab_layout_from_file("input.txt")
    walk_to_outside_of_lab(lab_layout)
    distinct_steps = get_number_of_distinct_moves(lab_layout)
    print(f"Number of distinct steps: {distinct_steps}")


if __name__ == "__main__":
    main()
