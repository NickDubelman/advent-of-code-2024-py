from part1 import load_input, Grid, Coord, in_bounds, update_guard_pos

"""
Notes from before solution:

- We can't brute force simulate every position in the grid
- We need a way to detect if a loop has been caused

Idea 1: For each coord in the grid, would introducing an obstacle here cause a loop? (brute force)

Idea 2: We don't need to check EVERY coord in the grid, only the coords the guard would visit if we
DIDN'T introduce an obstacle? --> yes, this approach worked

Even with Idea 2, it takes ~9 seconds to run... there's probably a better way
"""

def simulate_guard(grid: Grid) -> tuple[set[tuple[Coord, str]], bool]:
    # Determine the guard's starting position
    guard_dir: str = '^'
    guard_pos: Coord | None = None
    for i, row in enumerate(grid):
        try:
            guard_idx = row.index(guard_dir)
            if guard_idx != -1:
                guard_pos = (i, guard_idx)
                break
        except ValueError:
            pass

    assert guard_pos

    # To keep track of which position+directions we've visited, we'll use a set of (Coord, Dir)
    visited: set[tuple[Coord, str]] = set()

    while in_bounds(grid, guard_pos):
        # As long as the guard is still in bounds, keep updating their position

        # If we ever get to a position+direction that has already been visited, we have a loop
        if (guard_pos, guard_dir) in visited:
            # We have a loop
            return visited, True

        visited.add((guard_pos, guard_dir))
        guard_pos, guard_dir = update_guard_pos(grid, guard_pos, guard_dir)

    return visited, False

def main():
    grid = load_input()
    original_path, _ = simulate_guard(grid)

    original_coord_set = set([pos_dir[0] for pos_dir in original_path])

    count = 0
    for coord in original_coord_set:
        row_coord, col_coord = coord

        # Can't put an obstacle on the guard's original starting position
        if grid[row_coord][col_coord] == '^':
            continue

        # Put an obstacle at coord and then simulate if it causes a loop
        grid[row_coord][col_coord] = '#'

        _, has_loop = simulate_guard(grid)
        if has_loop:
            count += 1

        # Remove the obstacle now that we've simulated
        grid[row_coord][col_coord] = '.'
    
    print(count)

if __name__ == '__main__':
    main()