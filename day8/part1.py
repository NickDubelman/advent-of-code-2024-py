Grid = list[list[str]]
Coord = tuple[int, int]
Vector = tuple[int, int]


def load_input(filename="input.txt") -> Grid:
    with open(filename, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f]


def get_vector(coord1: Coord, coord2: Coord) -> Vector:
    return (coord2[0] - coord1[0], coord2[1] - coord1[1])


def in_bounds(row_len: int, col_len: int, coord: Coord) -> bool:
    row_coord, col_coord = coord
    if row_coord < 0 or row_coord >= row_len:
        return False
    if col_coord < 0 or col_coord >= col_len:
        return False
    return True


def main():
    grid = load_input()

    row_len = len(grid)
    assert row_len > 0
    col_len = len(grid[0])
    assert all([len(row) == col_len for row in grid])

    antenna_locations: dict[str, list[Coord]] = {}

    for i, row in enumerate(grid):
        for j in range(len(row)):
            char = grid[i][j]
            if char != ".":
                if char not in antenna_locations:
                    antenna_locations[char] = [(i, j)]
                else:
                    antenna_locations[char].append((i, j))

    antinode_locations: set[Coord] = set()
    for coords in antenna_locations.values():
        # Compare each coord to every other coord
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i != j:
                    coord1, coord2 = coords[i], coords[j]
                    row_vector, col_vector = get_vector(coord1, coord2)

                    antinode1 = (coord1[0] - row_vector, coord1[1] - col_vector)
                    antinode2 = (coord2[0] + row_vector, coord2[1] + col_vector)

                    if in_bounds(row_len, col_len, antinode1):
                        # grid[antinode1[0]][antinode1[1]] = "#"
                        antinode_locations.add(antinode1)
                    if in_bounds(row_len, col_len, antinode2):
                        # grid[antinode2[0]][antinode2[1]] = "#"
                        antinode_locations.add(antinode2)

    print(len(antinode_locations))


if __name__ == "__main__":
    main()
