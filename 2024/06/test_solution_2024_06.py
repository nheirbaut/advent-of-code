from solution_2024_06 import (
    create_lab_layout_from_lines,
    get_number_of_distinct_moves,
    walk_to_outside_of_lab,
)


def test_example_puzzle_input() -> None:
    """Test the example input from the puzzle."""
    test_lab_layout_str = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]
    test_lab_layout = create_lab_layout_from_lines(test_lab_layout_str)
    walk_to_outside_of_lab(test_lab_layout)
    assert get_number_of_distinct_moves(test_lab_layout) == 41  # noqa: PLR2004
