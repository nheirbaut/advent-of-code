MAX_VALUE_DISTANCE: int = 3

def is_safe_report_without_dampening(report: list[int]) -> bool:
    if len(report) == 1:
        return True

    current_level: int = report[0]

    levels_should_increase: bool = True

    if current_level > report[1]:
        levels_should_increase = False

    for level in report[1:]:
        if current_level == level:
            return False

        if levels_should_increase:
            if current_level > level:
                return False
        else:
            if current_level < level:
                return False

        if abs(current_level - level) > MAX_VALUE_DISTANCE:
            return False

        current_level = level

    return True

def is_safe_report_with_dampening(report: list[int]) -> bool:
    if is_safe_report_without_dampening(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report_without_dampening(modified_report):
            return True

    return False

def filter_safe_reports_without_dampening(reports: list[list[int]]) -> list[list[int]]:
    safe_reports: list[list[int]] = []

    for report in reports:
        if is_safe_report_without_dampening(report):
            safe_reports.append(report)

    return safe_reports

def filter_safe_reports_with_dampening(reports: list[list[int]]) -> list[list[int]]:
    safe_reports: list[list[int]] = []

    for report in reports:
        if is_safe_report_with_dampening(report):
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

    safe_reports = filter_safe_reports_without_dampening(reports)
    print(f"Number of safe reports: {len(safe_reports)}")

    safe_reports_after_dampening = filter_safe_reports_with_dampening(reports)
    print(f"Number of safe reports with dampening: {len(safe_reports_after_dampening)}")

if __name__ == "__main__":
    main()