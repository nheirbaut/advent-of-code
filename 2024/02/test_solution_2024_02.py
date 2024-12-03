from solution_2024_02 import (
    filter_safe_reports_with_dampening,
    filter_safe_reports_without_dampening,
)


def test_example_input():
    """
    Test the sample input provided in the puzzle description.
    """
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_empty_reports():
    """
    Test that the function returns 0 when there are no reports.
    """
    reports = []
    assert len(filter_safe_reports_without_dampening(reports)) == 0


def test_single_report_safe_increasing():
    """
    Test a single report that is safe and increasing.
    """
    reports = [[1, 2, 3, 4, 5]]
    assert len(filter_safe_reports_without_dampening(reports)) == 1


def test_single_report_safe_decreasing():
    """
    Test a single report that is safe and decreasing.
    """
    reports = [[5, 4, 3, 2, 1]]
    assert len(filter_safe_reports_without_dampening(reports)) == 1


def test_single_report_unsafe_mixed_direction():
    """
    Test a single report that is unsafe due to changing direction.
    """
    reports = [[1, 2, 1, 2, 1]]
    assert len(filter_safe_reports_without_dampening(reports)) == 0


def test_single_report_unsafe_large_difference():
    """
    Test a single report that is unsafe due to a large difference.
    """
    reports = [[1, 2, 10, 11, 12]]
    assert len(filter_safe_reports_without_dampening(reports)) == 0


def test_report_with_equal_adjacent_levels():
    """
    Test a report that is unsafe because it contains equal adjacent levels.
    """
    reports = [[1, 2, 2, 3, 4]]
    assert len(filter_safe_reports_without_dampening(reports)) == 0


def test_report_with_difference_of_one():
    """
    Test reports where adjacent levels differ by exactly one.
    """
    reports = [
        [1, 2, 3, 4, 5],  # Increasing
        [5, 4, 3, 2, 1],  # Decreasing
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_report_with_difference_of_three():
    """
    Test reports where adjacent levels differ by exactly three.
    """
    reports = [
        [1, 4, 7, 10, 13],  # Increasing
        [13, 10, 7, 4, 1],  # Decreasing
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_report_difference_out_of_bounds():
    """
    Test reports where adjacent levels differ by more than three or less than one.
    """
    reports = [
        [1, 5, 9, 13, 17],  # Difference of 4 (unsafe)
        [1, 1, 2, 3, 4],  # Difference of 0 between first two levels (unsafe)
        [5, 3, 1, -1, -3],  # Difference of 2 (safe)
        [5, 2, -1, -4, -7],  # Difference of 3 (safe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_report_mixed_increasing_decreasing():
    """
    Test reports that change direction (unsafe).
    """
    reports = [
        [1, 2, 3, 2, 1],  # Increases then decreases
        [5, 4, 5, 6, 7],  # Decreases then increases
        [1, 2, 3, 4, 5],  # Increasing (safe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 1


def test_report_with_single_level():
    """
    Test reports that contain only one level.
    """
    reports = [
        [5],  # Single level (safe by default)
        [10]   # Single level (safe by default)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_report_with_two_levels_safe():
    """
    Test reports with two levels that are safe.
    """
    reports = [
        [1, 3],  # Increasing by 2 (safe)
        [5, 2]   # Decreasing by 3 (safe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_report_with_two_levels_unsafe():
    """
    Test reports with two levels that are unsafe.
    """
    reports = [
        [1, 5],  # Increasing by 4 (unsafe)
        [5, 5]   # Difference of 0 (unsafe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 0


def test_negative_levels_safe():
    """
    Test reports with negative levels that are safe.
    """
    reports = [
        [-5, -4, -3, -2, -1],  # Increasing
        [0, -1, -2, -3, -4]    # Decreasing
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_negative_levels_unsafe():
    """
    Test reports with negative levels that are unsafe.
    """
    reports = [
        [-1, -2, -1, -2, -1],  # Changing direction
        [-1, -5, -9, -13, -17],  # Difference of 4 (unsafe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 0


def test_reports_with_zeros():
    """
    Test reports that include zeros.
    """
    reports = [
        [0, 1, 2, 3, 4],  # Increasing (safe)
        [0, -1, -2, -3],  # Decreasing (safe)
        [0, 0, 1, 2],  # Contains equal adjacent levels (unsafe)
        [0, 4, 8, 12],  # Difference of 4 (unsafe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_large_reports():
    """
    Test reports with a large number of levels.
    """
    reports = [
        list(range(1, 101)),  # Increasing by 1 (safe)
        list(range(100, 0, -2)),  # Decreasing by 2 (safe)
        list(range(0, 400, 4)),  # Difference of 4 (unsafe)
        [i**2 for i in range(1, 10)],  # Varying differences (unsafe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_reports_with_floats():
    """
    Optional: Test reports that include floating-point levels.
    """
    reports = [
        [1.0, 2.5, 4.0, 5.5],  # Increases by 1.5 (safe)
        [5.5, 4.0, 2.5, 1.0],  # Decreases by 1.5 (safe)
        [1.0, 1.0, 2.0, 3.0],  # Equal adjacent levels (unsafe)
        [1.0, 4.5, 8.0],  # Difference of 3.5 (unsafe)
    ]
    assert len(filter_safe_reports_without_dampening(reports)) == 2


def test_example_input_with_dampening():
    """
    Test the sample input provided in the puzzle description for Part Two.
    """
    reports = [
        [7, 6, 4, 2, 1],  # Safe without removing any level.
        [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed.
        [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed.
        [1, 3, 2, 4, 5],  # Safe by removing the second level, 3.
        [8, 6, 4, 4, 1],  # Safe by removing the third level, 4.
        [1, 3, 6, 7, 9],  # Safe without removing any level.
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 4


def test_reports_become_safe_after_removal():
    """
    Test reports that become safe by removing one level.
    """
    reports = [
        [1, 3, 2, 4, 5],  # Remove '3' to fix direction change.
        [1, 2, 3, 3, 4, 5],  # Remove one '3' to eliminate equal adjacent levels.
        [75, 77, 72, 70, 69],  # Remove '77' to make it safe
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 3


def test_reports_still_unsafe_after_removal():
    """
    Test reports that remain unsafe even after removing any one level.
    """
    reports = [
        [1, 2, 7, 8, 9],  # Differences too large.
        [1, 2, 3, 7, 8],  # Removing any level doesn't fix large difference.
        [1, 2, 1, 2, 1],  # Multiple direction changes.
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 0


def test_reports_already_safe():
    """
    Test reports that are already safe and should remain so.
    """
    reports = [
        [1, 2, 3, 4, 5],  # Increasing.
        [5, 4, 3, 2, 1],  # Decreasing.
        [1, 4, 7, 10],  # Increasing by 3.
        [13, 10, 7, 4, 1],  # Decreasing by 3.
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 4


def test_reports_with_equal_adjacent_levels():
    """
    Test reports that can become safe by removing a level with equal adjacent levels.
    """
    reports = [
        [1, 2, 2, 3, 4],  # Remove one '2' to fix equal levels.
        [1, 1, 2, 3, 4],  # Remove one '1'.
        [4, 4, 4, 4, 4],  # Cannot be made safe (no direction).
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 2


def test_reports_with_large_differences():
    """
    Test reports that can become safe by removing a level causing a large difference.
    """
    reports = [
        [1, 5, 9, 13, 17]  # Cannot be made safe (differences too large).
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 0


def test_single_level_reports():
    """
    Test reports that contain only one level.
    """
    reports = [
        [5],
        [10],
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 2


def test_two_level_reports():
    """
    Test reports with two levels.
    """
    reports = [
        [1, 2],  # Difference of 1 (safe).
        [1, 5],  # Difference of 4 (unsafe, can remove one level).
        [2, 2],  # Equal levels (unsafe, can remove one level).
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 3


def test_reports_with_negative_levels():
    """
    Test reports with negative levels that can become safe.
    """
    reports = [
        [-1, -2, -3, -4, -5],  # Decreasing (safe).
        [-5, -4, -3, -2, -1],  # Increasing (safe).
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 2


def test_reports_with_zeros_using_dampening():
    """
    Test reports that include zeros and can become safe after removing a level.
    """
    reports = [
        [0, 0, 1, 2],  # Remove one '0' to fix equal levels.
        [0, 4, 8, 12],  # Cannot be made safe (differences too large).
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 1


def test_large_reports_with_dampening():
    """
    Test reports with a large number of levels.
    """
    reports = [
        list(range(1, 101)),  # Increasing by 1 (safe).
        list(range(100, 0, -2)),  # Decreasing by 2 (safe).
        list(range(0, 400, 4)),  # Differences of 4 (unsafe, cannot be fixed).
        [i**2 for i in range(1, 10)],  # Varying differences (unsafe, cannot be fixed).
        list(range(1, 50))
        + [25]
        + list(range(51, 100)),  # Remove '25' to fix direction change.
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 3


def test_reports_that_cannot_be_fixed():
    """
    Test reports that cannot be made safe even after removing any one level.
    """
    reports = [
        [1, 2, 7, 8, 9],  # Differences too large.
        [1, 2, 1, 2, 1],  # Multiple direction changes.
        [1, 2, 3, 7, 8],  # Removing any level doesn't fix large difference.
    ]
    assert len(filter_safe_reports_with_dampening(reports)) == 0
