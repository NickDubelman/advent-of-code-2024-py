Grid = list[list[int]]
Coord = tuple[int, int]
Vector = tuple[int, int]

DIRECTIONS: list[Vector] = [
    (-1, 0),  # Up
    (0, -1),  # Left
    (0, 1),  # Right
    (1, 0),  # Down
]


def load_input(filename="input.txt") -> Grid:
    with open(filename, "r", encoding="utf-8") as f:
        return [[int(char) for char in line.strip()] for line in f]


def main():
    grid = load_input()

    row_len = len(grid)
    assert row_len > 0

    col_len = len(grid[0])
    assert all([len(row) == col_len for row in grid])

    def in_bounds(r: int, c: int) -> bool:
        return 0 <= r < row_len and 0 <= c < col_len

    trailheads: set[Coord] = set()

    # We will keep a mapping of a coordinate to each of its neighbors
    neighbor_map: dict[Coord, list[Coord]] = {}

    # We will memoize which trailends a coord can reach, so we dont have to recompute it
    trail_end_cache: dict[Coord, set[Coord]] = {}

    def get_trail_ends(coord: Coord) -> set[Coord]:
        if coord in trail_end_cache:
            return trail_end_cache[coord]

        if grid[coord[0]][coord[1]] == 9:
            trail_end_cache[coord] = {coord}
            return {coord}

        ends = set()
        for n in neighbor_map.get(coord, []):
            ends.update(get_trail_ends(n))

        trail_end_cache[coord] = ends
        return ends

    for i, row in enumerate(grid):
        for j in range(len(row)):
            if row[j] == 0:
                trailheads.add((i, j))

            if row[j] != 9:
                # If the coord is not the end of a trail, keep track of its neighbors
                for row_vector, col_vector in DIRECTIONS:
                    row_n, col_n = (i + row_vector, j + col_vector)
                    if in_bounds(row_n, col_n) and grid[row_n][col_n] - 1 == row[j]:
                        neighbor_map.setdefault((i, j), []).append((row_n, col_n))

    total = sum([len(get_trail_ends(t)) for t in trailheads])
    print(total)


if __name__ == "__main__":
    main()
