from year2024.day07.solution_2024_07 import (
    OPERATIONS_PART1,
    OPERATIONS_PART2,
    get_sum_total,
    parse_lines,
)


def test_puzzle_input_part1() -> None:
    """Test example puzzle input for Part 1."""
    test_input_lines = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]
    test_input = parse_lines(test_input_lines)
    assert get_sum_total(test_input, OPERATIONS_PART1) == 3749  # noqa: PLR2004


def test_puzzle_input_part2() -> None:
    """Test example puzzle input for Part 2."""
    test_input_lines = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]
    test_input = parse_lines(test_input_lines)
    assert get_sum_total(test_input, OPERATIONS_PART2) == 11387  # noqa: PLR2004
