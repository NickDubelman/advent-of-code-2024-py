from collections import Counter
from part1 import load_input, get_num_digits, split_num


def blink(stones: Counter) -> Counter:
    new_stones = Counter()

    for stone, count in stones.items():
        if stone == 0:
            # Convert the 0s to 1s
            new_stones[1] += count
        elif get_num_digits(stone) % 2 == 0:
            num1, num2 = split_num(stone)
            new_stones[num1] += count
            new_stones[num2] += count
        else:
            new_stones[stone * 2024] += count

    return new_stones


def main():
    stones = load_input()

    counter = Counter()
    for stone in stones:
        counter[stone] += 1

    for _ in range(75):
        counter = blink(counter)

    print(sum(counter.values()))


if __name__ == "__main__":
    main()
