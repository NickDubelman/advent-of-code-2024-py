def load_input(filename='example.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        return [list(map(int, line.split())) for line in f]

def is_safe(input: list[int]) -> bool:
    """{input} is considered safe if:
        - it is monotonically increasing/decreasing
        - all adjacent levels differ by 1, 2, or 3
    """
    if len(input) < 2:
        return True # Not sure if this will happen?

    if input[0] == input[1]:
        return False # Must differ by at least 1
    elif input[0] < input[1]:
        increasing = True
    else:
        increasing = False

    for i in range(len(input) - 1):
        if increasing:
            diff = input[i+1] - input[i]
        else:
            diff = input[i] - input[i+1]

        if not 1 <= diff <= 3:
            return False

    return True

def main():
    lines = load_input()
    safe_count = [is_safe(line) for line in lines].count(True)
    print(safe_count)

if __name__ == '__main__':
    main()