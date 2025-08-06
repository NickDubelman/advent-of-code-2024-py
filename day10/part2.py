from part1 import load_input, Coord, DIRECTIONS


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
    num_path_cache: dict[Coord, int] = {}

    def get_num_paths(coord: Coord) -> int:
        if coord in num_path_cache:
            return num_path_cache[coord]

        if grid[coord[0]][coord[1]] == 9:
            num_path_cache[coord] = 1
            return 1

        count = sum([get_num_paths(n) for n in neighbor_map.get(coord, [])])
        num_path_cache[coord] = count
        return count

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

    total = sum([get_num_paths(t) for t in trailheads])
    print(total)


if __name__ == "__main__":
    main()
