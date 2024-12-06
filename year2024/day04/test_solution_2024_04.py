from year2024.day04.solution_2024_04 import (
    count_number_of_occurrences,
    count_number_of_x_mas_occurrences,
)


def test_xmas_occurrences_in_example() -> None:
    """Test the example input provided in the problem description."""
    test_word = "XMAS"
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    assert count_number_of_occurrences(word_search, test_word) == 18  # noqa: PLR2004


def test_x_mas_occurrences_in_example() -> None:
    """Test the example input for X-MAS occurrences."""
    test_word = "MAS"
    word_search = [
        ".M.S......",
        "..A..MSMS.",
        ".M.S.MAA..",
        "..A.ASMSM.",
        ".M.S.M....",
        "..........",
        "S.S.S.S.S.",
        ".A.A.A.A..",
        "M.M.M.M.M.",
        "..........",
    ]
    assert count_number_of_x_mas_occurrences(word_search, test_word) == 9  # noqa: PLR2004
