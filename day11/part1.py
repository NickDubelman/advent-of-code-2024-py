def load_input(filename="input.txt") -> list[int]:
    with open(filename, "r", encoding="utf-8") as f:
        return [int(char) for line in f for char in line.split()]


def get_num_digits(n: int) -> int:
    if n < 0:
        raise ValueError()
    return len(str((n)))


def split_num(n: int) -> tuple[int, int]:
    n_str = str(n)
    split_idx = len(n_str) // 2
    num1 = n_str[:split_idx]
    num2 = n_str[split_idx:]
    return int(num1), int(num2)


def blink(stones: list[int]) -> list[int]:
    new_stones: list[int] = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif get_num_digits(stone) % 2 == 0:
            new_stones += list(split_num(stone))
        else:
            new_stones.append(stone * 2024)

    return new_stones


def main():
    stones = load_input()

    for _ in range(25):
        stones = blink(stones)

    print(len(stones))


if __name__ == "__main__":
    main()
