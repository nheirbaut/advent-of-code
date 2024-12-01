# import pytest

from solution import calculate_similarity_score

def test_sample_input():
    """
    Test the sample input provided in the puzzle description.
    """
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert calculate_similarity_score(left_list, right_list) == 31

def test_empty_lists():
    """
    Test that the function returns 0 when both lists are empty.
    """
    left_list = []
    right_list = []
    assert calculate_similarity_score(left_list, right_list) == 0

def test_no_common_elements():
    """
    Test the function with lists that have no common elements.
    """
    left_list = [1, 2, 3]
    right_list = [4, 5, 6]
    assert calculate_similarity_score(left_list, right_list) == 0

def test_negative_numbers():
    """
    Test the function with negative numbers in the lists.
    """
    left_list = [-1, -2, -3, -1]
    right_list = [-1, -1, -4, -5]
    # Calculations:
    # -1 appears 2 times in right_list: -1 * 2 = -2 (for each occurrence in left_list)
    # Total similarity score = (-1 * 2) + (-2 * 0) + (-3 * 0) + (-1 * 2) = -2 + 0 + 0 + -2 = -4
    assert calculate_similarity_score(left_list, right_list) == -4

def test_zeros():
    """
    Test the function when zeros are included in the lists.
    """
    left_list = [0, 0, 1]
    right_list = [0, 2, 0]
    # Calculations:
    # 0 appears 2 times in right_list: 0 * 2 = 0 (for each 0 in left_list)
    # 1 appears 0 times: 1 * 0 = 0
    # Total similarity score = 0 + 0 + 0 = 0
    assert calculate_similarity_score(left_list, right_list) == 0

def test_duplicate_numbers():
    """
    Test the function with duplicate numbers in the left list.
    """
    left_list = [2, 2, 2]
    right_list = [2, 2, 3]
    # Calculations:
    # 2 appears 2 times in right_list: 2 * 2 = 4 (for each occurrence in left_list)
    # Total similarity score = 4 + 4 + 4 = 12
    assert calculate_similarity_score(left_list, right_list) == 12

def test_large_numbers():
    """
    Test the function with large numbers to ensure it handles big integers.
    """
    left_list = [1000000, 2000000, 3000000]
    right_list = [3000000, 2000000, 1000000, 1000000]
    # Calculations:
    # 1000000 appears 2 times: 1000000 * 2 = 2000000
    # 2000000 appears 1 time: 2000000 * 1 = 2000000
    # 3000000 appears 1 time: 3000000 * 1 = 3000000
    # Total similarity score = 2000000 + 2000000 + 3000000 = 7000000
    assert calculate_similarity_score(left_list, right_list) == 7000000

def test_single_element_lists():
    """
    Test the function with single-element lists.
    """
    left_list = [5]
    right_list = [5]
    # 5 appears 1 time: 5 * 1 = 5
    assert calculate_similarity_score(left_list, right_list) == 5

def test_left_list_repeats_right_list_once():
    """
    Test when left list has repeated numbers and right list has unique numbers.
    """
    left_list = [1, 1, 1, 1]
    right_list = [1]
    # 1 appears 1 time in right_list: 1 * 1 = 1 (for each occurrence in left_list)
    # Total similarity score = 1 + 1 + 1 + 1 = 4
    assert calculate_similarity_score(left_list, right_list) == 4

def test_right_list_empty():
    """
    Test when the right list is empty; similarity score should be zero.
    """
    left_list = [1, 2, 3]
    right_list = []
    assert calculate_similarity_score(left_list, right_list) == 0

def test_right_list_has_more_occurrences():
    """
    Test when right list has more occurrences of a number than left list.
    """
    left_list = [2, 3]
    right_list = [2, 2, 2, 3, 3]
    # 2 appears 3 times: 2 * 3 = 6
    # 3 appears 2 times: 3 * 2 = 6
    # Total similarity score = 6 + 6 = 12
    assert calculate_similarity_score(left_list, right_list) == 12

def test_different_length_lists():
    """
    Test that the function handles lists of different lengths.
    """
    left_list = [1, 2, 3, 4, 5]
    right_list = [2, 2, 3]
    # Calculations:
    # 1 appears 0 times: 1 * 0 = 0
    # 2 appears 2 times: 2 * 2 = 4
    # 3 appears 1 time: 3 * 1 = 3
    # 4 appears 0 times: 4 * 0 = 0
    # 5 appears 0 times: 5 * 0 = 0
    # Total similarity score = 0 + 4 + 3 + 0 + 0 = 7
    assert calculate_similarity_score(left_list, right_list) == 7
