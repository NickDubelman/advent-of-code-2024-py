from part1 import load_input

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

def is_safe_with_tolerance(input: list[int]) -> bool:
    if is_safe(input):
        return True
    
    # If the list isn't safe, see if a single number can be removed to make it safe
    def without_i(i: int) -> list[int]:
        return input[:i] + input[i+1:]
    
    for i in range(len(input)):
        if is_safe(without_i(i)):
            return True

    return False

def main():
    lines = load_input()
    safe_count = [is_safe_with_tolerance(line) for line in lines].count(True)
    print(safe_count)

if __name__ == '__main__':
    main()