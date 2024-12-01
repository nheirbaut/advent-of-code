def calculate_total_distance(left_list: list[int], right_list: list[int]) -> int:
    if len(left_list) != len(right_list):
        raise ValueError("Lists must be of the same length")

    return sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))

def read_columns(file_path: str) -> tuple[list[int], list[int]]:
    left_list: list[int] = []
    right_list: list[int] = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                values = line.split()
                left_list.append(int(values[0]))
                right_list.append(int(values[1]))

    return left_list, right_list

def main():
    left_list, right_list = read_columns("input.txt")
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance: {total_distance}")

if __name__ == "__main__":
    main()