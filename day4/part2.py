from part1 import load_input, Coord, WordSearch

# Not actually used but useful reminder
# BOTTOM_LEFT_TOP_RIGHT_DIAGONAL = [(1,-1), (-1,1)]
# TOP_LEFT_BOTTOM_RIGHT_DIAGONAL = [(-1,-1), (1,1)]

class WordSearchX(WordSearch):
    def __init__(self, grid: list[list[str]], first_char: str, pivot_char: str, last_char: str):
        super().__init__(grid)
        self.first_char = first_char
        self.pivot_char = pivot_char
        self.last_char = last_char

    def check_diagonal(self, coord1: Coord, coord2: Coord) -> bool:
        # Make sure both coords are in bounds
        if not self.in_bounds(coord1) or not self.in_bounds(coord2):
            return False

        char_set: set[str] = {
            self.grid[coord1[0]][coord1[1]],
            self.grid[coord2[0]][coord2[1]]
        }
        
        # Set must have 2 elements and they must be {first_char} and {last_char}
        if len(char_set) != 2:
            return False

        return self.first_char in char_set and self.last_char in char_set

    def count(self) -> int:
        count = 0
        for i in range(self.row_count):
            for j in range(self.col_count):
                if self.grid[i][j] == self.pivot_char:
                    bottom_left, top_right = (i+1,j-1), (i-1,j+1)
                    top_left, bottom_right = (i-1,j-1), (i+1,j+1)

                    # All corners are in bounds, check the 2 diagonal directions
                    # First diagonal
                    if not self.check_diagonal(bottom_left, top_right):
                        continue

                    # Second diagonal
                    if not self.check_diagonal(top_left, bottom_right):
                        continue

                    count += 1

        return count

def main():
    char_grid = load_input()
    
    # FIXME: For now just hardcode the word and assume it always has length 3
    word = 'MAS'
    assert len(word) == 3 

    first_char: str = word[0]
    pivot_char: str = word[1] # {pivot_char} is the "center of the X"
    last_char: str = word[2]

    search = WordSearchX(char_grid, first_char, pivot_char, last_char )
    count = search.count()
    print(count)

if __name__ == '__main__':
    main()