Point = tuple[int, int]
Grid = dict[Point, str]


def create_grid_from_lines(lines: list[str]) -> Grid:
    """Create a grid with points from a list with strings definition.

    Args:
        lines (list[str]): All lines describing the grid

    Returns:
        Grid: The created grid
    """
    grid: Grid = {}

    for row_index, line in enumerate(lines):
        for column_index, value in enumerate(line):
            grid[column_index, row_index] = value

    return grid


def find_first_point_for_value(grid: Grid, target_value: str) -> Point | None:
    """Find the first point in the grid containing a given value.

    Args:
        grid (Grid): The grid to search
        target_value (str): The value to find

    Returns:
        Point | None: First point with the value or None when not found
    """
    for point, value in grid.items():
        if target_value == value:
            return point

    return None
