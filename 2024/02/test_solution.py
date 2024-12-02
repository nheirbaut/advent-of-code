from solution import filter_safe_reports

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
        [1, 3, 6, 7, 9]
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_empty_reports():
    """
    Test that the function returns 0 when there are no reports.
    """
    reports = []
    assert len(filter_safe_reports(reports)) == 0

def test_single_report_safe_increasing():
    """
    Test a single report that is safe and increasing.
    """
    reports = [[1, 2, 3, 4, 5]]
    assert len(filter_safe_reports(reports)) == 1

def test_single_report_safe_decreasing():
    """
    Test a single report that is safe and decreasing.
    """
    reports = [[5, 4, 3, 2, 1]]
    assert len(filter_safe_reports(reports)) == 1

def test_single_report_unsafe_mixed_direction():
    """
    Test a single report that is unsafe due to changing direction.
    """
    reports = [[1, 2, 1, 2, 1]]
    assert len(filter_safe_reports(reports)) == 0

def test_single_report_unsafe_large_difference():
    """
    Test a single report that is unsafe due to a large difference.
    """
    reports = [[1, 2, 10, 11, 12]]
    assert len(filter_safe_reports(reports)) == 0

def test_report_with_equal_adjacent_levels():
    """
    Test a report that is unsafe because it contains equal adjacent levels.
    """
    reports = [[1, 2, 2, 3, 4]]
    assert len(filter_safe_reports(reports)) == 0

def test_report_with_difference_of_one():
    """
    Test reports where adjacent levels differ by exactly one.
    """
    reports = [
        [1, 2, 3, 4, 5],   # Increasing
        [5, 4, 3, 2, 1]    # Decreasing
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_report_with_difference_of_three():
    """
    Test reports where adjacent levels differ by exactly three.
    """
    reports = [
        [1, 4, 7, 10, 13],  # Increasing
        [13, 10, 7, 4, 1]   # Decreasing
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_report_difference_out_of_bounds():
    """
    Test reports where adjacent levels differ by more than three or less than one.
    """
    reports = [
        [1, 5, 9, 13, 17],  # Difference of 4 (unsafe)
        [1, 1, 2, 3, 4],    # Difference of 0 between first two levels (unsafe)
        [5, 3, 1, -1, -3],  # Difference of 2 (safe)
        [5, 2, -1, -4, -7]  # Difference of 3 (safe)
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_report_mixed_increasing_decreasing():
    """
    Test reports that change direction (unsafe).
    """
    reports = [
        [1, 2, 3, 2, 1],  # Increases then decreases
        [5, 4, 5, 6, 7],  # Decreases then increases
        [1, 2, 3, 4, 5]   # Increasing (safe)
    ]
    assert len(filter_safe_reports(reports)) == 1

def test_report_with_single_level():
    """
    Test reports that contain only one level.
    """
    reports = [
        [5],  # Single level (safe by default)
        [10], # Single level (safe by default)
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_report_with_two_levels_safe():
    """
    Test reports with two levels that are safe.
    """
    reports = [
        [1, 3],  # Increasing by 2 (safe)
        [5, 2],  # Decreasing by 3 (safe)
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_report_with_two_levels_unsafe():
    """
    Test reports with two levels that are unsafe.
    """
    reports = [
        [1, 5],  # Increasing by 4 (unsafe)
        [5, 5],  # Difference of 0 (unsafe)
    ]
    assert len(filter_safe_reports(reports)) == 0

def test_negative_levels_safe():
    """
    Test reports with negative levels that are safe.
    """
    reports = [
        [-5, -4, -3, -2, -1],  # Increasing
        [0, -1, -2, -3, -4]    # Decreasing
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_negative_levels_unsafe():
    """
    Test reports with negative levels that are unsafe.
    """
    reports = [
        [-1, -2, -1, -2, -1],  # Changing direction
        [-1, -5, -9, -13, -17] # Difference of 4 (unsafe)
    ]
    assert len(filter_safe_reports(reports)) == 0

def test_reports_with_zeros():
    """
    Test reports that include zeros.
    """
    reports = [
        [0, 1, 2, 3, 4],  # Increasing (safe)
        [0, -1, -2, -3],  # Decreasing (safe)
        [0, 0, 1, 2],     # Contains equal adjacent levels (unsafe)
        [0, 4, 8, 12]     # Difference of 4 (unsafe)
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_large_reports():
    """
    Test reports with a large number of levels.
    """
    reports = [
        list(range(1, 101)),        # Increasing by 1 (safe)
        list(range(100, 0, -2)),    # Decreasing by 2 (safe)
        list(range(0, 400, 4)),     # Difference of 4 (unsafe)
        [i**2 for i in range(1, 10)] # Varying differences (unsafe)
    ]
    assert len(filter_safe_reports(reports)) == 2

def test_reports_with_floats():
    """
    Optional: Test reports that include floating-point levels.
    """
    reports = [
        [1.0, 2.5, 4.0, 5.5],  # Increases by 1.5 (safe)
        [5.5, 4.0, 2.5, 1.0],  # Decreases by 1.5 (safe)
        [1.0, 1.0, 2.0, 3.0],  # Equal adjacent levels (unsafe)
        [1.0, 4.5, 8.0],       # Difference of 3.5 (unsafe)
    ]
    assert len(filter_safe_reports(reports)) == 2
