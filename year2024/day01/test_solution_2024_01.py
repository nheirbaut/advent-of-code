import pytest

from year2024.day01.solution_2024_01 import (
    calculate_similarity_score,
    calculate_total_distance,
)

# Tests for calculate_similarity_score


def test_calculate_similarity_score_sample_input() -> None:
    """Test the sample input provided in the puzzle."""
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert calculate_similarity_score(left_list, right_list) == 31  # noqa: PLR2004


def test_calculate_similarity_score_empty_lists() -> None:
    """Test that calculate_similarity_score returns 0 when both lists are empty."""
    left_list = []
    right_list = []
    assert calculate_similarity_score(left_list, right_list) == 0


def test_calculate_similarity_score_no_common_elements() -> None:
    """Test calculate_similarity_score with lists that have no common elements."""
    left_list = [1, 2, 3]
    right_list = [4, 5, 6]
    assert calculate_similarity_score(left_list, right_list) == 0


def test_calculate_similarity_score_negative_numbers() -> None:
    """Test calculate_similarity_score with negative numbers in the lists."""
    left_list = [-1, -2, -3, -1]
    right_list = [-1, -1, -4, -5]
    # Calculations:
    # -1 appears 2 times in right_list: -1 * 2 = -2 (for each occurrence in left_list)
    # Total similarity score = (-1 * 2) + (-2 * 0) + (-3 * 0) + (-1 * 2) = -4
    assert calculate_similarity_score(left_list, right_list) == -4  # noqa: PLR2004


def test_calculate_similarity_score_zeros() -> None:
    """Test calculate_similarity_score when zeros are included in the lists."""
    left_list = [0, 0, 1]
    right_list = [0, 2, 0]
    # Calculations:
    # 0 appears 2 times in right_list: 0 * 2 = 0 (for each 0 in left_list)
    # 1 appears 0 times: 1 * 0 = 0
    # Total similarity score = 0 + 0 + 0 = 0
    assert calculate_similarity_score(left_list, right_list) == 0


def test_calculate_similarity_score_duplicate_numbers() -> None:
    """Test calculate_similarity_score with duplicate numbers in the left list."""
    left_list = [2, 2, 2]
    right_list = [2, 2, 3]
    # Calculations:
    # 2 appears 2 times in right_list: 2 * 2 = 4 (for each occurrence in left_list)
    # Total similarity score = 4 + 4 + 4 = 12
    assert calculate_similarity_score(left_list, right_list) == 12  # noqa: PLR2004


def test_calculate_similarity_score_large_numbers() -> None:
    """Test it handles big integers."""
    left_list = [1000000, 2000000, 3000000]
    right_list = [3000000, 2000000, 1000000, 1000000]
    # Calculations:
    # 1000000 appears 2 times: 1000000 * 2 = 2000000
    # 2000000 appears 1 time: 2000000 * 1 = 2000000
    # 3000000 appears 1 time: 3000000 * 1 = 3000000
    # Total similarity score = 2000000 + 2000000 + 3000000 = 7000000
    assert calculate_similarity_score(left_list, right_list) == 7000000  # noqa: PLR2004


def test_calculate_similarity_score_single_element_lists() -> None:
    """Test calculate_similarity_score with single-element lists."""
    left_list = [5]
    right_list = [5]
    # 5 appears 1 time: 5 * 1 = 5
    assert calculate_similarity_score(left_list, right_list) == 5  # noqa: PLR2004


def test_calculate_similarity_score_left_list_repeats_right_list_once() -> None:
    """Test left list has repeated numbers and right list has unique numbers."""
    left_list = [1, 1, 1, 1]
    right_list = [1]
    # 1 appears 1 time in right_list: 1 * 1 = 1 (for each occurrence in left_list)
    # Total similarity score = 1 + 1 + 1 + 1 = 4
    assert calculate_similarity_score(left_list, right_list) == 4  # noqa: PLR2004


def test_calculate_similarity_score_right_list_empty() -> None:
    """Test the right list is empty; similarity score should be zero."""
    left_list = [1, 2, 3]
    right_list = []
    assert calculate_similarity_score(left_list, right_list) == 0


def test_calculate_similarity_score_right_list_has_more_occurrences() -> None:
    """Test right list has more occurrences of a number than left list."""
    left_list = [2, 3]
    right_list = [2, 2, 2, 3, 3]
    # 2 appears 3 times: 2 * 3 = 6
    # 3 appears 2 times: 3 * 2 = 6
    # Total similarity score = 6 + 6 = 12
    assert calculate_similarity_score(left_list, right_list) == 12  # noqa: PLR2004


def test_calculate_similarity_score_different_length_lists() -> None:
    """Test that calculate_similarity_score handles lists of different lengths."""
    left_list = [1, 2, 3, 4, 5]
    right_list = [2, 2, 3]
    # Calculations:
    # 1 appears 0 times: 1 * 0 = 0
    # 2 appears 2 times: 2 * 2 = 4
    # 3 appears 1 time: 3 * 1 = 3
    # 4 appears 0 times: 4 * 0 = 0
    # 5 appears 0 times: 5 * 0 = 0
    # Total similarity score = 0 + 4 + 3 + 0 + 0 = 7
    assert calculate_similarity_score(left_list, right_list) == 7  # noqa: PLR2004


# Tests for calculate_total_distance


def test_calculate_total_distance_sample_input() -> None:
    """Test the sample input provided in the puzzle description."""
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert calculate_total_distance(left_list, right_list) == 11  # noqa: PLR2004


def test_calculate_total_distance_empty_lists() -> None:
    """Test that calculate_total_distance returns 0 when both lists are empty."""
    left_list = []
    right_list = []
    assert calculate_total_distance(left_list, right_list) == 0


def test_calculate_total_distance_single_element_lists() -> None:
    """Test calculate_total_distance with single-element lists."""
    left_list = [5]
    right_list = [10]
    assert calculate_total_distance(left_list, right_list) == 5  # noqa: PLR2004


def test_calculate_total_distance_negative_numbers() -> None:
    """Test calculate_total_distance with negative numbers in the lists."""
    left_list = [-1, -2, -3]
    right_list = [1, 2, 3]
    assert calculate_total_distance(left_list, right_list) == 12  # noqa: PLR2004


def test_calculate_total_distance_zeros() -> None:
    """Test calculate_total_distance when all elements are zero."""
    left_list = [0, 0, 0]
    right_list = [0, 0, 0]
    assert calculate_total_distance(left_list, right_list) == 0


def test_calculate_total_distance_duplicate_numbers() -> None:
    """Test calculate_total_distance with duplicate numbers in the lists."""
    left_list = [1, 1, 1, 1]
    right_list = [2, 2, 2, 2]
    assert calculate_total_distance(left_list, right_list) == 4  # noqa: PLR2004


def test_calculate_total_distance_large_numbers() -> None:
    """Test it handles big integers."""
    left_list = [1000000, 2000000, 3000000]
    right_list = [3000000, 2000000, 1000000]
    assert calculate_total_distance(left_list, right_list) == 0


def test_calculate_total_distance_different_length_lists() -> None:
    """Test that a ValueError is raised when lists have different lengths."""
    left_list = [1, 2, 3]
    right_list = [4, 5]
    with pytest.raises(ValueError):  # noqa: PT011
        calculate_total_distance(left_list, right_list)
