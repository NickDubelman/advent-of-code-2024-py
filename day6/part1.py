Grid = list[list[str]]
Coord = tuple[int, int]
Vector = tuple[int, int]

# Lookup a current direction and get the next direction
next_direction: dict[str, str] = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

direction_vector: dict[str, Vector] = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

def load_input(filename='example-input.txt') -> Grid:
    with open(filename, 'r', encoding='utf-8') as f:
        grid = [list(line.strip()) for line in f]
        
        assert len(grid) > 0 # Must have at least one row
        
        col_len = len(grid[0])
        assert col_len > 0 # Must have at least one col
        assert all([len(row) == col_len for row in grid]) # All columns must have same length
        
        return grid
    
def update_guard_pos(grid: Grid, curr_pos: Coord, curr_direction: str) -> tuple[Coord, str]:
    "Returns ({new_position}, {new_direction})"

    row_vec, col_vec = direction_vector[curr_direction]

    curr_row, curr_col = curr_pos
    potential_next_pos = (curr_row + row_vec, curr_col + col_vec)

    if in_bounds(grid, potential_next_pos):
        # Check if the potential next position has an obstacle (#)
        if grid[potential_next_pos[0]][potential_next_pos[1]] == '#':
            # Guard has hit an obstacle, stay in same position and rotate direction
            new_direction = next_direction[curr_direction]
            return curr_pos, new_direction
    
    # Next position does NOT have an obstacle
    return potential_next_pos, curr_direction


def in_bounds(grid: Grid, coord: Coord):
    row_len = len(grid)
    col_len = len(grid[0])

    row, col = coord
    if row < 0 or row >= row_len:
        return False
    
    if col < 0 or col >= col_len:
        return False
    
    return True

def simulate_guard(grid: Grid) -> set[Coord]:
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

    # To keep track of which coordinates we've visited, we'll use a set of Coord
    visited: set[Coord] = {guard_pos}

    # Don't need the path to solve, but used it for debugging
    path: list[Coord] = []

    while in_bounds(grid, guard_pos):
        # As long as the guard is still in bounds, keep updating their position
        visited.add(guard_pos)
        path.append(guard_pos)
        guard_pos, guard_dir = update_guard_pos(grid, guard_pos, guard_dir)

    return visited


def main():
    grid = load_input()
    visited = simulate_guard(grid)
    print(len(visited))

if __name__ == '__main__':
    main()
