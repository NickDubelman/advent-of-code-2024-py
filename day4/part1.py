def load_input(filename='input.txt') -> list[list[str]]:
    with open(filename, 'r', encoding='utf-8') as f:
        # Read the lines into a grid (2d-list)
        return [list(line.strip()) for line in f]

Coord = tuple[int, int]
Vector = tuple[int, int]

DIRECTIONS = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1),
]

class WordSearch():
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.row_count = len(grid)
        assert self.row_count > 0
        self.col_count = len(grid[0])
        assert(all(len(row) == self.col_count for row in self.grid))
    
    def in_bounds(self, coord: Coord) -> bool:
        return 0 <= coord[0] < self.row_count and 0 <= coord[1] < self.col_count

    def dfs_in_direction(self, coord: Coord, direction: Vector, word: str, char_idx: int) -> bool:
        if char_idx == len(word) :
            return True # reached end of word
        
        row_idx, col_idx = coord
        row_vector, col_vector = direction
        new_row_idx, new_col_idx = row_idx + row_vector, col_idx + col_vector
        new_coord = (new_row_idx, new_col_idx)

        if not self.in_bounds(new_coord):
            return False
        if self.grid[new_row_idx][new_col_idx] != word[char_idx]:
            return False
    
        return self.dfs_in_direction(new_coord, direction, word, char_idx + 1)

    def count_word(self, word: str) -> int:
        assert len(word) > 1 # Assume we are never just looking for a single letter

        count = 0
        for i in range(self.row_count):
            for j in range(self.col_count):
                if self.grid[i][j] == word[0]:
                    for dr, dc in DIRECTIONS:
                        curr_coord = (i, j)
                        direction_vector = (dr, dc)
                        if self.dfs_in_direction(curr_coord, direction_vector, word, 1):
                            count += 1

        return count

def main():
    char_grid = load_input()
    
    search = WordSearch(char_grid)
    count = search.count_word('XMAS')
    print(count)

if __name__ == '__main__':
    main()