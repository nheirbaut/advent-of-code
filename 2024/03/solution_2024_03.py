import re

def find_all_instructions(memory: str) -> list[str]:
    return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", memory)

def get_mul_arguments(instruction: str) -> tuple[int, int]:
    f1, f2 = map(int, instruction[4:-1].split(","))
    return f1, f2

def sum_mul_instructions(instructions: list[str]) -> int:
    sum_total = 0

    for instruction in instructions:
        if instruction[0] == 'd':
            continue

        f1, f2 = get_mul_arguments(instruction)

        sum_total += f1 * f2

    return sum_total

def sum_enabled_mul_instructions(instructions: list[str]) -> int:
    sum_total = 0

    enabled = True

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
            continue

        if instruction == "don't()":
            enabled = False
            continue

        if enabled:
            f1, f2 = get_mul_arguments(instruction)
            sum_total += f1 * f2

    return sum_total

def get_input(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()

def main() -> None:
    memory = get_input("/workspaces/advent-of-code/2024/03/input.txt")

    instructions = find_all_instructions(memory)

    part1_solution = sum_mul_instructions(instructions)
    print(f"Solution part 1: {part1_solution}")

    part2_solution = sum_enabled_mul_instructions(instructions)
    print(f"Solution part 2: {part2_solution}")

if __name__ == '__main__':
    main()
