from solution_2024_04 import count_number_of_occurrences


def test_occurrences_in_example() -> None:
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
