def is_safe_report(report: list[int]) -> bool:
    if len(report) == 1:
        return True

    current_value: int = report[0]

    levels_should_increase: bool = True

    if current_value > report[1]:
        levels_should_increase = False

    for value in report[1:]:
        if current_value == value:
            return False

        if levels_should_increase:
            if current_value > value:
                return False
        else:
            if current_value < value:
                return False

        if abs(current_value - value) > 3:
            return False

        current_value = value

    return True


def filter_safe_reports(reports: list[list[int]]) -> list[list[int]]:
    safe_reports: list[list[int]] = []

    for report in reports:
        if is_safe_report(report):
            safe_reports.append(report)

    return safe_reports

def read_reports(file_path: str) -> list[list[int]]:
    reports: list[list[int]] = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                reports.append(list(map(int, line.split())))

    return reports

def main():
    reports = read_reports("input.txt")
    safe_reports = filter_safe_reports(reports)
    print(f"Number of safe reports: {len(safe_reports)}")

if __name__ == "__main__":
    main()