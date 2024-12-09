from collections.abc import Callable
from pathlib import Path

OPERATIONS_PART1: list[Callable[[int, int], int]] = [
    lambda x, y: x + y,  # '+' operator
    lambda x, y: x * y,  # '*' operator
]

OPERATIONS_PART2: list[Callable[[int, int], int]] = [
    lambda x, y: x + y,  # '+' operator
    lambda x, y: x * y,  # '*' operator
    lambda x, y: int(f"{x}{y}"),  # '||' operator
]


def try_find_successful_solution(
    total: int,
    numbers: list[int],
    already_known_good_or_bad_totals: dict[tuple[tuple[int, ...], int], bool],
    operations: list[Callable[[int, int], int]],
) -> int | None:
    """Try to find a succesfull solution recursively.

    Args:
        total (int): The total to look for
        numbers (list[int]): The numbers to try the operations on
        already_known_good_or_bad_totals (dict[tuple[tuple[int, ...], int], bool]):
            already known good and bad combinations
        operations (list[Callable[[int, int], int]]): The allowed operations

    Returns:
        int | None: The found total if possible, None otherwise
    """
    if len(numbers) == 1:
        return total if total == numbers[0] else None

    current_total_and_numbers = (tuple(numbers), total)
    if current_total_and_numbers in already_known_good_or_bad_totals:
        return already_known_good_or_bad_totals[current_total_and_numbers]

    first, second = numbers[0], numbers[1]

    for operation in operations:
        new_numbers: list[int] = [operation(first, second)] + numbers[2:]

        if try_find_successful_solution(
            total, new_numbers, already_known_good_or_bad_totals, operations
        ):
            already_known_good_or_bad_totals[current_total_and_numbers] = True
            return total

    already_known_good_or_bad_totals[current_total_and_numbers] = False

    return None


def get_sum_total(
    totals_and_numbers: list[tuple[int, list[int]]],
    operations: list[Callable[[int, int], int]],
) -> int:
    """Get the sum total for all valid solutions.

    Args:
        totals_and_numbers (list[tuple[int, list[int]]]):
            The list of totals and their possible solution numbers
        operations (list[Callable[[int, int], int]]): The allowed operations

    Returns:
        int: The total for all valid solutions
    """
    sum_total = 0

    for total, numbers in totals_and_numbers:
        memo: dict[tuple[tuple[int, ...], int], bool] = {}
        if try_find_successful_solution(total, numbers, memo, operations):
            sum_total += total

    return sum_total


def read_all_lines_from_file(file_path: str) -> list[str]:
    """Read all the lines from the given file.

    Args:
        file_path (str): The file to read the lines from

    Returns:
        list[str]: The read lines
    """
    with Path(file_path).open() as file:
        return [line.rstrip() for line in file]


def parse_lines(lines: list[str]) -> list[tuple[int, list[int]]]:
    """Parse the given lines to correct input for this puzzle.

    Args:
        lines (list[str]): The lines to parse

    Returns:
        list[tuple[int, list[int]]]: The totals and their numbers after parsing
    """
    totals_and_numbers: list[tuple[int, list[int]]] = []

    for line in lines:
        total_part, numbers_part = line.split(":")
        total = int(total_part.strip())
        numbers = list(map(int, numbers_part.strip().split()))
        totals_and_numbers.append((total, numbers))

    return totals_and_numbers


def main() -> None:
    """Main entry point for this application."""
    lines = read_all_lines_from_file(
        "/workspaces/advent-of-code/year2024/day07/input.txt"
    )

    totals_and_numbers = parse_lines(lines)

    sum_total = get_sum_total(totals_and_numbers, OPERATIONS_PART1)
    print(f"Solution Part 1: {sum_total}")

    sum_total = get_sum_total(totals_and_numbers, OPERATIONS_PART2)
    print(f"Solution Part 2: {sum_total}")


if __name__ == "__main__":
    main()
