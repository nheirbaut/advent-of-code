from itertools import cycle
from pathlib import Path

from utils.grid import Grid, Point, create_grid_from_lines, find_first_point_for_value

type DirectionDelta = tuple[int, int]
type DirectionDeltas = list[DirectionDelta]


def add_delta_to_point(point: Point, delta: Point) -> Point:
    """Add given delta to given point.

    Args:
        point (Point): Point to add to
        delta (Point): Delta to add

    Returns:
        Point: The adjusted point
    """
    return point[0] + delta[0], point[1] + delta[1]


def find_exit_path(lab_grid: Grid) -> tuple[bool, set[Point]]:
    """Find a possible exit path.

    Args:
        lab_grid (Grid): The grid to find the exit from

    Returns:
        tuple[bool, set[Point]]: True and the path when exited,
          False and an empty set otherwise
    """
    up_delta = (0, -1)
    down_delta = (0, 1)
    left_delta = (-1, 0)
    right_delta = (1, 0)

    possible_direction_deltas: cycle[DirectionDelta] = cycle(
        [
            up_delta,
            right_delta,
            down_delta,
            left_delta,
        ]
    )

    current_direction_delta = next(possible_direction_deltas)

    current_location = find_first_point_for_value(lab_grid, "^")
    assert current_location is not None

    visited_locations_from_direction: set[tuple[Point, DirectionDelta]] = {
        (current_location, current_direction_delta)
    }

    while True:
        next_location = add_delta_to_point(current_location, current_direction_delta)
        if next_location not in lab_grid:
            # Moved out of the lab
            break

        if lab_grid[next_location] == "#":
            current_direction_delta = next(possible_direction_deltas)
            visited_locations_from_direction.add(
                (current_location, current_direction_delta)
            )
            continue

        if (next_location, current_direction_delta) in visited_locations_from_direction:
            # Been here before from the same direction, so stuck in a loop
            return False, set()

        visited_locations_from_direction.add((next_location, current_direction_delta))
        current_location = next_location

    return True, {location for location, _ in visited_locations_from_direction}


def prevent_guard_from_moving_out(lab_grid: Grid) -> int:
    """Prevent the guard from moving out of the lab by adding obstacles.

    Args:
        lab_grid (Grid): A grid describing the lab

    Returns:
        int: The number of obstacles added
    """
    exited, succesful_exit_path = find_exit_path(lab_grid)
    assert exited

    possible_obstacle_locations = 0
    for current_location in succesful_exit_path:
        if lab_grid[current_location] == "^":
            continue

        lab_grid[current_location] = "#"
        exited, _ = find_exit_path(lab_grid)
        if not exited:
            possible_obstacle_locations += 1

        lab_grid[current_location] = "."

    return possible_obstacle_locations


def main() -> None:
    """Main entry point for the application."""
    lines: list[str] = []
    with Path("input.txt").open() as file:
        lines = [line.rstrip() for line in file]

    lab_grid = create_grid_from_lines(lines)
    _, path = find_exit_path(lab_grid)
    print(f"Number of distinct steps: {len(path)}")

    lab_grid = create_grid_from_lines(lines)
    obstacles_added = prevent_guard_from_moving_out(lab_grid)
    print(f"Obstacles added: {obstacles_added}")


if __name__ == "__main__":
    main()
