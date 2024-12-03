from collections import Counter
from pathlib import Path


def calculate_total_distance(left_list: list[int], right_list: list[int]) -> int:
    """Calculate the total distance between two lists of integers.

    The total distance is computed by:
    - Sorting both lists.
    - Pairing up the smallest numbers, second smallest, etc.
    - Summing the absolute differences between each pair.

    Args:
        left_list (list[int]): The first list of integers.
        right_list (list[int]): The second list of integers.

    Returns:
        int: The total distance between the two lists.

    Raises:
        ValueError: If the input lists are not of the same length.

    """
    if len(left_list) != len(right_list):
        raise ValueError("Lists must be of the same length")

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    return sum(abs(left - right) for left, right in zip(sorted_left, sorted_right, strict=False))


def calculate_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    """Calculate the similarity score between two lists of integers.

    The similarity score is computed by:
    - Counting the frequency of each number in the right list.
    - For each number in the left list, multiplying it by its frequency in the right list.
    - Summing these products.

    Args:
        left_list (list[int]): The first list of integers.
        right_list (list[int]): The second list of integers.

    Returns:
        int: The similarity score between the two lists.

    """
    frequency_table = Counter(right_list)
    return sum(num * frequency_table.get(num, 0) for num in left_list)


def read_columns(file_path: str) -> tuple[list[int], list[int]]:
    """Read two columns of integers from a file and return them as two separate lists.

    Each line in the file should contain two integers separated by whitespace.
    Empty lines are skipped.

    Args:
        file_path (str): The path to the input file.

    Returns:
        tuple[list[int], list[int]]: A tuple containing two lists of integers.

    Raises:
        ValueError: If a line does not contain two integers.
        ValueError: If a value cannot be converted to an integer.

    """
    left_list: list[int] = []
    right_list: list[int] = []

    with Path(file_path).open() as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line:
                values = line.split()
                if len(values) == 2:
                    try:
                        left_value = int(values[0])
                        right_value = int(values[1])
                        left_list.append(left_value)
                        right_list.append(right_value)
                    except ValueError as e:
                        raise ValueError(f"Line {line_number}: {e}")
                else:
                    raise ValueError(
                        f"Line {line_number}: Expected at two values, got {len(values)}"
                    )

    return left_list, right_list


def main() -> None:
    """Main function to read input data, calculate total distance and similarity score, and print the results."""
    try:
        left_list, right_list = read_columns("input.txt")
        total_distance = calculate_total_distance(left_list, right_list)
        print(f"Total distance: {total_distance}")

        similarity_score = calculate_similarity_score(left_list, right_list)
        print(f"Similarity score: {similarity_score}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
