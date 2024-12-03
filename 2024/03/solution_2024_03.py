import re
from pathlib import Path


def find_all_instructions(memory: str) -> list[str]:
    """Extract all valid instructions from the memory string.

    Valid instructions are:
    - mul(n1,n2): where n1 and n2 are 1 to 3 digit integers.
    - do()
    - don't()

    Args:
        memory (str): The corrupted memory string.

    Returns:
        list[str]: A list of valid instruction strings.
    """
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    return re.findall(pattern, memory)


def get_mul_arguments(instruction: str) -> tuple[int, int]:
    """Parse a mul instruction and extract its numerical arguments.

    Args:
        instruction (str): A valid mul instruction in the form 'mul(n1,n2)'.

    Returns:
        tuple[int, int]: A tuple containing the two integer arguments.

    Raises:
        ValueError: If the instruction is not a valid mul instruction.
    """
    args = instruction[4:-1]
    n1_str, n2_str = args.split(",")
    n1 = int(n1_str)
    n2 = int(n2_str)
    return n1, n2


def sum_mul_instructions(instructions: list[str]) -> int:
    """Calculate the sum of the results of all valid mul instructions.

    Args:
        instructions (List[str]): A list of instruction strings.

    Returns:
        int: The sum of the multiplication results.
    """
    total = 0

    for instruction in instructions:
        if instruction.startswith("mul("):
            n1, n2 = get_mul_arguments(instruction)
            total += n1 * n2

    return total


def sum_enabled_mul_instructions(instructions: list[str]) -> int:
    """Calculate the sum of the results of enabled mul instructions.

    Args:
        instructions (List[str]): A list of instruction strings.

    Returns:
        int: The sum of the multiplication results of enabled mul instructions.
    """
    total = 0
    enabled = True

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul(") and enabled:
            n1, n2 = get_mul_arguments(instruction)
            total += n1 * n2

    return total


def get_input(file_path: str) -> str:
    """Read the content of the input file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        str: The content of the file as a string.
    """
    with Path(file_path).open() as file:
        return file.read()


def main() -> None:
    """Main entry point for the application."""
    memory = get_input("input.txt")

    instructions = find_all_instructions(memory)

    part1_solution = sum_mul_instructions(instructions)
    print(f"Solution Part 1: {part1_solution}")

    part2_solution = sum_enabled_mul_instructions(instructions)
    print(f"Solution Part 2: {part2_solution}")


if __name__ == "__main__":
    main()
