import time


def load_input(filename="input.txt") -> list[int]:
    with open(filename, "r", encoding="utf-8") as f:
        return [int(char) for line in f for char in list(line)]


class DiskMap:
    def __init__(self, input: list[int]):
        # We want to parse the input and put into a list[int | None]
        # For example: 12345 -> 0..111....22222 which is represented as [0, None, None, 1, ...]

        file_blocks = [value for idx, value in enumerate(input) if idx % 2 == 0]
        free_space_blocks = [value for idx, value in enumerate(input) if idx % 2 != 0]

        assert len(free_space_blocks) == len(file_blocks) - 1

        id = 0
        value: list[int | None] = []
        for i, block in enumerate(file_blocks):
            # Add {id} to {value} based on the number given by {block}
            for _ in range(block):
                value.append(id)

            # Next, add None to value based on the number given by corresponding free space block
            if i < len(free_space_blocks):
                for _ in range(free_space_blocks[i]):
                    value.append(None)

            id += 1

        self.value = value

    def __repr__(self) -> str:
        return self.represent_disk_map_value(self.value)

    @staticmethod
    def represent_disk_map_value(value: list[int | None]) -> str:
        # ex: [0, None, None, 1, 1, 1, None, ...] -> 0..111....22222
        return "".join(["." if v is None else str(v) for v in value])

    def compact(self) -> list[int | None]:
        start = time.perf_counter()

        value = self.value.copy()  # We don't want to mutate self.value directly

        left = 0
        right = len(value) - 1

        while left < right:
            # Move left to first None spot
            while left < right and value[left] is not None:
                left += 1

            # Move right to first non-None spot
            while right > left and value[right] is None:
                right -= 1

            if left < right:
                value[left] = value[right]
                value[right] = None
                left += 1
                right -= 1

        end = time.perf_counter()
        print(f"compact took {end - start:.6f} seconds")

        return [val for val in value if val is not None]

    def checksum(self) -> int:
        compacted = self.compact()

        result = 0
        for i, val in enumerate(compacted):
            if val is not None:
                result += i * val

        return result


def main():
    input = load_input()

    disk_map = DiskMap(input)
    print(disk_map.checksum())


if __name__ == "__main__":
    main()
