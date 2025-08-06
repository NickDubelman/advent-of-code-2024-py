import re
from part1 import load_input

def calc(input: str) -> int:
    sum = 0

    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for match in matches:
        nums = re.findall(r"\d+", match)
        assert len(nums) == 2
        sum += int(nums[0]) * int(nums[1])

    return sum

def evaluate_input(input: str, acc: int) -> int:    
    # Find index of the first instance of "don't()"
    dont_idx = input.find("don't()")

    # If no more don't(), just process the full input 
    if dont_idx == -1:
        return acc + calc(input)
    
    # Get everything before the "don't()"
    consider = input[:dont_idx]
    sum_consider = calc(consider)

    # Find the first do() after the don't()
    rest = input[dont_idx:]
    next_do_idx = rest.find("do()")
    next = rest[next_do_idx:]

    return acc + sum_consider + evaluate_input(next, acc)


def main():
    input = load_input()
    sum = evaluate_input(input, 0)
    print(sum)

if __name__ == '__main__':
    main()