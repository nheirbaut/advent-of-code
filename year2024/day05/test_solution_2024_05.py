from solution_2024_05 import (
    get_corrected_updates,
    get_rules_from_lines,
    get_updates_from_lines,
    get_valid_and_invalid_updates,
    sum_of_all_middle_values,
)


def test_sum_of_all_middle_values() -> None:
    """Test calculating the sum of all middle values."""
    test_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sum_of_all_middle_values(test_values) == 15  # noqa: PLR2004


def test_get_updates_from_lines() -> None:
    """Test getting update values from lines of input."""
    test_lines = [
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]
    expected_updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    assert get_updates_from_lines(test_lines) == expected_updates


def test_get_rules_from_lines() -> None:
    """Test getting the rules from lines of input."""
    test_lines = [
        "01|05",
        "02|04",
        "03|03",
        "04|02",
        "05|01",
        "01|02",
        "02|03",
        "03|04",
        "04|05",
    ]
    expected_before_rules = {1: [5, 2], 2: [4, 3], 3: [3, 4], 4: [2, 5], 5: [1]}
    before_rules = get_rules_from_lines(test_lines)
    assert before_rules == expected_before_rules


def test_example_puzzle_input() -> None:
    """Test the puzzle example."""
    test_updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    test_rule_lines = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    expected_valid_updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
    ]
    expected_invalid_updates = [
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    test_before_rules = get_rules_from_lines(test_rule_lines)
    valid_updates, invalid_updates = get_valid_and_invalid_updates(
        test_updates, test_before_rules
    )
    assert valid_updates == expected_valid_updates
    assert invalid_updates == expected_invalid_updates


def test_update_correction() -> None:
    """Test correcting invalid updates."""
    test_invalid_updates = [
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    test_rule_lines = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    expected_corrected_rules = [
        [97, 75, 47, 61, 53],
        [61, 29, 13],
        [97, 75, 47, 29, 13],
    ]
    test_before_rules = get_rules_from_lines(test_rule_lines)
    assert (
        get_corrected_updates(test_invalid_updates, test_before_rules)
        == expected_corrected_rules
    )
