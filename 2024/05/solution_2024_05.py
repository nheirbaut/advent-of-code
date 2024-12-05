from pathlib import Path


def sum_of_all_middle_values(values: list[list[int]]) -> int:
    """Calculate the sum of all middle values of all given lists.

    Args:
        values (list[list[int]]): The lists to calculate the sum for

    Returns:
        int: The sum of all middle values of all given lists
    """
    return sum(sublist[len(sublist) // 2] for sublist in values)


def get_all_lines_from_file(file_path: str) -> list[str]:
    """Read all lines from a given file.

    Args:
        file_path (str): The file to read the lines from

    Returns:
        list[str]: All read lines
    """
    with Path(file_path).open() as file:
        all_lines = file.readlines()
        return [line.rstrip() for line in all_lines]


def get_rules_from_lines(
    rule_lines: list[str],
) -> dict[int, list[int]]:
    """Determine the page rules from the given line definitions.

    Args:
        rule_lines (list[str]): A list representing th erules

    Returns:
        dict[int, list[int]]: The rules per page
    """
    before_rules: dict[int, list[int]] = {}

    for rule_line in rule_lines:
        page1, page2 = map(int, rule_line.split("|"))

        if page1 not in before_rules:
            before_rules[page1] = []
        before_rules[page1].append(page2)

    return before_rules


def get_rules_from_file(
    file_path: str,
) -> dict[int, list[int]]:
    """Determine the page rules from the given file.

    Args:
        file_path (str): The file to load the rules from

    Returns:
        dict[int, list[int]]: The rules per page
    """
    rule_lines = get_all_lines_from_file(file_path)
    return get_rules_from_lines(rule_lines)


def get_updates_from_lines(update_lines: list[str]) -> list[list[int]]:
    """Get the updates to validate.

    Args:
        update_lines (list[str]): The string representation of the updates to validate

    Returns:
        list[list[int]]: The numeric representation of the updates to validate
    """
    return [list(map(int, update_line.split(","))) for update_line in update_lines]


def get_updates_from_file(file_path: str) -> list[list[int]]:
    """Get the updates to validate from file.

    Args:
        file_path (str): The file to get the updates from

    Returns:
        list[list[int]]: The numeric representation of the updates to validate
    """
    update_lines = get_all_lines_from_file(file_path)
    return get_updates_from_lines(update_lines)


def get_valid_updates(
    updates: list[list[int]],
    before_rules: dict[int, list[int]],
) -> list[list[int]]:
    """Get the valid updates.

    Args:
        updates (list[list[int]]): The updates to validate
        before_rules (dict[int, list[int]]): The rules to validate for

    Returns:
        list[list[int]]: The validated updates
    """
    valid_updates: list[list[int]] = []

    for update in updates:
        valid = True

        for page_index, page_number in enumerate(update):
            if page_number in before_rules:
                must_be_before_pages = before_rules[page_number]

                pages_preceding = update[:page_index]
                if any(
                    page_preceding in must_be_before_pages
                    for page_preceding in pages_preceding
                ):
                    valid = False
                    break

            pages_following = update[page_index + 1 :]
            for page_following in pages_following:
                if page_following in before_rules:
                    following_page_before_rule = before_rules[page_following]
                    if page_number in following_page_before_rule:
                        valid = False
                        break

            if not valid:
                break

        if valid:
            valid_updates.append(update)

    return valid_updates


def main() -> None:
    """Main entry point for the application."""
    before_rules = get_rules_from_file("rules.txt")
    updates = get_updates_from_file("input.txt")

    valid_updates = get_valid_updates(updates, before_rules)

    sum1 = sum_of_all_middle_values(valid_updates)
    print(f"The sum is: {sum1}")


if __name__ == "__main__":
    main()
