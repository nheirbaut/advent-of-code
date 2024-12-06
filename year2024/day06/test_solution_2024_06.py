from solution_2024_06 import (
    find_exit_path,
    prevent_guard_from_moving_out,
)
from utils.grid import create_grid_from_lines


def test_example_puzzle_input_for_succesful_exit() -> None:
    """Test the example input from the puzzle for succesful exit."""
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
    test_lab_grid = create_grid_from_lines(test_lab_layout_str)
    exited, path = find_exit_path(test_lab_grid)
    assert exited
    assert len(path) == 41  # noqa: PLR2004


def test_example_puzzle_input_for_added_obstacles() -> None:
    """Test the example input from the puzzle for added obstacles."""
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
    test_lab_grid = create_grid_from_lines(test_lab_layout_str)
    assert prevent_guard_from_moving_out(test_lab_grid) == 6  # noqa: PLR2004
