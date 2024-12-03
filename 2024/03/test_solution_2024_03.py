from solution_2024_03 import (
    find_all_instructions,
    sum_enabled_mul_instructions,
    sum_mul_instructions,
)

# Tests for find_all_instructions


def test_find_all_instructions_example():
    """Test the example input provided in the problem description.
    """
    memory = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64]then(mul(11,8)do()?mul(8,5))"
    )
    expected_instructions = [
        "mul(2,4)",
        "don't()",
        "mul(5,5)",
        "mul(11,8)",
        "do()",
        "mul(8,5)",
    ]
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_no_valid_instructions():
    """Test input with no valid instructions.
    """
    memory = "This is some random text without any valid instructions."
    assert find_all_instructions(memory) == []


def test_find_all_instructions_only_invalid_instructions():
    """Test input containing only invalid instructions.
    """
    memory = "mul(4*, mul(6,9!, ?(12,34), mul ( 2 , 4 )"
    assert find_all_instructions(memory) == []


def test_find_all_instructions_multiple_valid_instructions():
    """Test input with multiple valid instructions.
    """
    memory = "mul(12,34)mul(56,78)mul(90,1)"
    expected_instructions = ["mul(12,34)", "mul(56,78)", "mul(90,1)"]
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_mixed_valid_and_invalid():
    """Test input with a mix of valid and invalid instructions.
    """
    memory = "mul(10,20)invalidmul(30,40)mul(50,60)mul(7,8,9)"
    expected_instructions = ["mul(10,20)", "mul(30,40)", "mul(50,60)"]
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_with_do_and_dont():
    """Test input containing valid do() and don't() instructions.
    """
    memory = "mul(1,1)don't()mul(2,2)do()mul(3,3)don't()mul(4,4)do()mul(5,5)"
    expected_instructions = [
        "mul(1,1)",
        "don't()",
        "mul(2,2)",
        "do()",
        "mul(3,3)",
        "don't()",
        "mul(4,4)",
        "do()",
        "mul(5,5)",
    ]
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_with_invalid_do_and_dont():
    """Test that invalid do() and don't() instructions are ignored.
    """
    memory = "do(n't)mul(2,2)do()mul(3,3)don('t)mul(4,4)don't()mul(5,5)"
    expected_instructions = [
        "mul(2,2)",
        "do()",
        "mul(3,3)",
        "mul(4,4)",
        "don't()",
        "mul(5,5)",
    ]
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_with_spaces():
    """Test that instructions with spaces are not included.
    """
    memory = "mul(9,9) mul(8, 8)mul(7,7)"
    expected_instructions = [
        "mul(9,9)",
        "mul(7,7)",
    ]  # Only mul(9,9) and mul(7,7) are valid
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_with_leading_trailing_spaces():
    """Test that leading and trailing spaces are handled correctly.
    """
    memory = "  mul(1,2)  don't()  mul(3,4)  "
    expected_instructions = ["mul(1,2)", "don't()", "mul(3,4)"]
    assert find_all_instructions(memory) == expected_instructions


def test_find_all_instructions_empty_input():
    """Test that an empty input string returns an empty list.
    """
    memory = ""
    assert find_all_instructions(memory) == []


# Tests for sum_mul_instructions


def test_sum_mul_instructions_example():
    """Test sum_mul_instructions with the example instructions.
    """
    instructions = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]
    expected_sum = (2 * 4) + (5 * 5) + (11 * 8) + (8 * 5)  # 8 + 25 + 88 + 40 = 161
    assert sum_mul_instructions(instructions) == expected_sum


def test_sum_mul_instructions_no_mul_instructions():
    """Test with no mul instructions.
    """
    instructions = ["don't()", "do()"]
    assert sum_mul_instructions(instructions) == 0


def test_sum_mul_instructions_with_leading_zeros():
    """Test mul instructions with leading zeros.
    """
    instructions = ["mul(001,002)", "mul(03,004)"]
    expected_sum = (1 * 2) + (3 * 4)  # 2 + 12 = 14
    assert sum_mul_instructions(instructions) == expected_sum


def test_sum_mul_instructions_zero():
    """Test mul instructions with zero as a number.
    """
    instructions = ["mul(0,5)", "mul(6,0)", "mul(0,0)"]
    expected_sum = 0  # All results are zero
    assert sum_mul_instructions(instructions) == expected_sum


def test_sum_mul_instructions_empty_list():
    """Test sum_mul_instructions with an empty list.
    """
    instructions = []
    assert sum_mul_instructions(instructions) == 0


# Tests for sum_enabled_mul_instructions


def test_sum_enabled_mul_instructions_example():
    """Test sum_enabled_mul_instructions with the example instructions.
    """
    instructions = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]
    expected_sum = (2 * 4) + (8 * 5)  # 8 + 40 = 48
    assert sum_enabled_mul_instructions(instructions) == expected_sum


def test_sum_enabled_mul_instructions_no_mul_instructions():
    """Test with no mul instructions.
    """
    instructions = ["don't()", "do()"]
    assert sum_enabled_mul_instructions(instructions) == 0


def test_sum_enabled_mul_instructions_initially_enabled():
    """Test that initial state is enabled.
    """
    instructions = ["mul(1,1)", "don't()", "mul(2,2)", "do()", "mul(3,3)"]
    expected_sum = (1 * 1) + (3 * 3)  # 1 + 9 = 10
    assert sum_enabled_mul_instructions(instructions) == expected_sum


def test_sum_enabled_mul_instructions_all_disabled():
    """Test with all mul instructions disabled.
    """
    instructions = ["don't()", "mul(1,1)", "mul(2,2)", "mul(3,3)"]
    assert sum_enabled_mul_instructions(instructions) == 0


def test_sum_enabled_mul_instructions_enable_disable():
    """Test with multiple do() and don't() instructions.
    """
    instructions = [
        "mul(1,1)",
        "don't()",
        "mul(2,2)",
        "do()",
        "mul(3,3)",
        "don't()",
        "mul(4,4)",
        "do()",
        "mul(5,5)",
    ]
    expected_sum = (1 * 1) + (3 * 3) + (5 * 5)  # 1 + 9 + 25 = 35
    assert sum_enabled_mul_instructions(instructions) == expected_sum


def test_sum_enabled_mul_instructions_zero():
    """Test with zero multiplications.
    """
    instructions = ["do()", "mul(0,5)", "don't()", "mul(5,0)", "do()", "mul(0,0)"]
    expected_sum = (0 * 5) + (0 * 0)  # Both results are zero
    assert sum_enabled_mul_instructions(instructions) == expected_sum


def test_sum_enabled_mul_instructions_empty_list():
    """Test sum_enabled_mul_instructions with an empty list.
    """
    instructions = []
    assert sum_enabled_mul_instructions(instructions) == 0


def test_sum_enabled_mul_instructions_do_and_dont_at_end():
    """Test that do() or don't() at the end affects future instructions only.
    """
    instructions = ["mul(1,1)", "do()", "don't()"]
    expected_sum = 1 * 1
    assert sum_enabled_mul_instructions(instructions) == expected_sum


def test_sum_enabled_mul_instructions_multiple_do_or_dont():
    """Test multiple do() or don't() instructions in a row.
    """
    instructions = ["don't()", "don't()", "mul(2,2)", "do()", "do()", "mul(3,3)"]
    expected_sum = 3 * 3  # Only the last do() applies
    assert sum_enabled_mul_instructions(instructions) == expected_sum


def test_sum_enabled_mul_instructions_with_zero_multiplications():
    """Test that zero multiplications are included if enabled.
    """
    instructions = ["do()", "mul(0,5)", "don't()", "mul(5,0)", "do()", "mul(0,0)"]
    expected_sum = (0 * 5) + (0 * 0)  # Both results are zero
    assert sum_enabled_mul_instructions(instructions) == expected_sum
