import pytest

from solution import calculate_total_distance

def test_sample_input():
    """
    Test the sample input provided in the puzzle description.
    """
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert calculate_total_distance(left_list, right_list) == 11

def test_empty_lists():
    """
    Test that the function returns 0 when both lists are empty.
    """
    left_list = []
    right_list = []
    assert calculate_total_distance(left_list, right_list) == 0

def test_single_element_lists():
    """
    Test the function with single-element lists.
    """
    left_list = [5]
    right_list = [10]
    assert calculate_total_distance(left_list, right_list) == 5

def test_negative_numbers():
    """
    Test the function with negative numbers in the lists.
    """
    left_list = [-1, -2, -3]
    right_list = [1, 2, 3]
    assert calculate_total_distance(left_list, right_list) == 12

def test_zeros():
    """
    Test the function when all elements are zero.
    """
    left_list = [0, 0, 0]
    right_list = [0, 0, 0]
    assert calculate_total_distance(left_list, right_list) == 0

def test_duplicate_numbers():
    """
    Test the function with duplicate numbers in the lists.
    """
    left_list = [1, 1, 1, 1]
    right_list = [2, 2, 2, 2]
    assert calculate_total_distance(left_list, right_list) == 4

def test_large_numbers():
    """
    Test the function with large numbers to ensure it handles big integers.
    """
    left_list = [1000000, 2000000, 3000000]
    right_list = [3000000, 2000000, 1000000]
    assert calculate_total_distance(left_list, right_list) == 0

def test_different_length_lists():
    """
    Test that the function raises a ValueError when lists have different lengths.
    """
    left_list = [1, 2, 3]
    right_list = [4, 5]
    with pytest.raises(ValueError):
        calculate_total_distance(left_list, right_list)
