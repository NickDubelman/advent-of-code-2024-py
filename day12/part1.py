Coord = tuple[int, int]


def load_input(filename="example-input.txt") -> list[list[str]]:
    with open(filename, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f]


def main():
    grid = load_input()

    row_len = len(grid)
    assert row_len > 0
    col_len = len(grid[0])
    assert all([len(row) == col_len for row in grid])

    def in_bounds(i: int, j: int) -> bool:
        return 0 <= i < row_len and 0 <= j < col_len

    explored: set[Coord] = set()

    # Mapping of area "ID" to its cost (which is area*perimeter)
    area_costs: dict[int, int] = {}

    curr_area_id = 0

    def explore(coord: Coord, plant_type: str, region: set[Coord]) -> int:
        """Returns perimeter"""
        row_coord, col_coord = coord

        explored.add((row_coord, col_coord))
        region.add((row_coord, col_coord))

        perimeter = 0
        neighbor_perimeter = 0

        for row_vector, col_vector in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr, nc = row_coord + row_vector, col_coord + col_vector
            neighbor = (nr, nc)

            if not in_bounds(nr, nc):
                perimeter += 1
            elif grid[nr][nc] != plant_type:
                perimeter += 1
            elif neighbor not in explored:
                neighbor_perimeter += explore(neighbor, plant_type, region)

        return perimeter + neighbor_perimeter

    for i, row in enumerate(grid):
        for j in range(len(row)):
            if (i, j) in explored:
                continue  # Skip if already visited

            plant_type = grid[i][j]
            curr_area_id += 1

            region: set[Coord] = set()
            perim = explore((i, j), plant_type, region)
            area_costs[curr_area_id] = len(region) * perim

    print(sum(area_costs.values()))


if __name__ == "__main__":
    main()
