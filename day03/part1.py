import re

def load_input(filename='input.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    input = load_input()
    
    sum = 0

    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for match in matches:
        nums = re.findall(r"\d+", match)
        assert len(nums) == 2
        sum += int(nums[0]) * int(nums[1])

    print(sum)

if __name__ == '__main__':
    main()