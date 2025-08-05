from part1 import load_input, DiskMap


class DiskMap2(DiskMap):
    """
    DiskMap2 has a different compaction algorithm than DiskMap (but the same checksumming)
    """

    def __init__(self, input: list[int]):
        super().__init__(input)

    def get_free_space(self) -> dict[int, int]:
        """
        Iterate through value and find all of the free space
        Store it as a mapping of index -> number of open spaces
        """

        free_space: dict[int, int] = {}

        curr_available_space = 0
        for i, v in enumerate(self.value):
            # If we get to a taken index and we've been accumulating available space, it's the end
            if v is not None and curr_available_space != 0:
                free_space[i - curr_available_space] = curr_available_space
                curr_available_space = 0

            if v is None:
                curr_available_space += 1

            i += 1

        return free_space

    def compact(self):
        free_space = self.get_free_space()

        value = self.value.copy()  # We don't want to mutate self.value directly

        # Iterate from the end and try to move contiguous file blocks into open space
        # Need to update {free_space} dict as we mutate {value}
        right = len(value) - 1

        curr_id: int | None = value[right]
        required_space = 0

        while right > 0:
            # If in an open space and we aren't looking for an ID, just move to next iteration
            if value[right] is None and curr_id is None:
                right -= 1
                continue

            if value[right] == curr_id:
                # We are accumulating an ongoing block
                required_space += 1
            else:
                # We've gotten to the end of the block for the ID we are looking for
                # Find the first open space of size >= {required_space} (if there is any)
                can_move = any([s >= required_space for s in free_space.values()])
                if can_move:
                    # There is a position with sufficient open space
                    min_idx = min(
                        [
                            idx
                            for idx, space in free_space.items()
                            if space >= required_space
                        ]
                    )
                    curr_idx = min_idx

                    # Only do the move if {min_idx} is less than {right}
                    # Otherwise, we could be moving a block backwards, which we don't want
                    if min_idx <= right:
                        # Populate {required_space} spots, starting with min_idx
                        while required_space > 0:
                            # Move the digit
                            value[curr_idx] = curr_id
                            value[right + required_space] = None

                            curr_idx += 1
                            required_space -= 1

                            # Update {free_space} to reflect the space that was just occupied
                            free_space[curr_idx] = free_space[curr_idx - 1] - 1
                            del free_space[curr_idx - 1]

                        # Check if {free_space[curr_idx]} has been used up
                        if free_space[curr_idx] == 0:
                            del free_space[curr_idx]

                curr_id = value[right]
                required_space = 0 if curr_id is None else 1

            right -= 1

        return value


def main():
    input = load_input()

    disk_map = DiskMap2(input)
    print(disk_map.checksum())


if __name__ == "__main__":
    main()
