from part1 import load_input

def get_possible_results(nums: list[int]) -> set[int]:
    def dfs(current_value: int, nums: list[int]) -> set[int]:
        if len(nums) == 0:
            return {current_value}
                
        num1, *rest = nums
        add_options = dfs(current_value + num1, rest)
        mult_options = dfs(current_value * num1, rest)
        concat_options = dfs(int(str(current_value) + str(num1)), rest)

        return add_options | mult_options | concat_options # Set union is like set addition
    
    return dfs(nums[0], nums[1:])

def main():
    calibrations = load_input()

    result = 0
    for c in calibrations:
        if c[0] in get_possible_results(c[1]):
            result += c[0]
    print(result)

if __name__ == '__main__':
    main()