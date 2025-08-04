from part1 import load_input, Coord, get_vector, in_bounds


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
                    while in_bounds(row_len, col_len, antinode1):
                        antinode_locations.add(antinode1)
                        antinode1 = (
                            antinode1[0] - row_vector,
                            antinode1[1] - col_vector,
                        )

                    antinode2 = (coord1[0] + row_vector, coord1[1] + col_vector)
                    while in_bounds(row_len, col_len, antinode2):
                        antinode_locations.add(antinode2)
                        antinode2 = (
                            antinode2[0] + row_vector,
                            antinode2[1] + col_vector,
                        )

    print(len(antinode_locations))


if __name__ == "__main__":
    main()
