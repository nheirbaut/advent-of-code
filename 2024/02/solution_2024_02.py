MAX_VALUE_DISTANCE = 3

def is_safe_report_without_dampening(report: list[int]) -> bool:
    """
    Determines if a report is safe without applying the Problem Dampener.

    A report is safe if:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    - There are no equal adjacent levels.
    """
    if len(report) <= 1:
        return True

    current_level = report[0]

    levels_should_increase = True

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
    """
    Determines if a report is safe, possibly after removing one level.

    The Problem Dampener allows removing one level to make the report safe.
    """
    if is_safe_report_without_dampening(report):
        return True

    # Try removing each level one at a time
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report_without_dampening(modified_report):
            return True

    return False

def filter_safe_reports_without_dampening(reports: list[list[int]]) -> list[list[int]]:
    """
    Filters and returns the list of safe reports without applying the Problem Dampener.
    """
    return [report for report in reports if is_safe_report_without_dampening(report)]

def filter_safe_reports_with_dampening(reports: list[list[int]]) -> list[list[int]]:
    """
    Filters and returns the list of safe reports, applying the Problem Dampener.
    """
    return [report for report in reports if is_safe_report_with_dampening(report)]

def read_reports(file_path: str) -> list[list[int]]:
    """
    Reads reports from a file and returns them as a list of lists of integers.
    """
    reports = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
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
