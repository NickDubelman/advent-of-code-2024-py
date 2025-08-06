from collections.abc import Callable

def load_input(filename='input.txt') -> tuple[list[list[int]], list[list[int]]]:
    with open(filename, 'r', encoding='utf-8') as f:
        parts = f.read().split('\n\n')
        assert len(parts) >= 2
        part1, part2 = parts[0], parts[1]

        ordering_rules = [list(map(int, line.split('|'))) for line in part1.splitlines()]
        updates = [list(map(int, line.split(','))) for line in part2.splitlines()]

        return (ordering_rules, updates)

def get_rule_fn(rule: list[int]) -> Callable[[list[int]], bool]:
    num1, num2 = rule
    def rule_fn(update: list[int]) -> bool:
        update_set = set(update)

        # If the update doesn't contain both numbers from the rule, it passes
        if num1 not in update_set or num2 not in update_set:
            return True
        
        # If the update does contain both numbers, {num1} must come first
        return update.index(num1) < update.index(num2)
    
    return rule_fn

def get_mid_value(numbers: list[int]) -> int:
    num_len = len(numbers)
    assert num_len % 2 == 1 # numbers must have odd len
    return numbers[num_len // 2]

def main():
    ordering_rules, updates = load_input()
    
    # Accumulate a list of functions that take an update and return a bool
    rule_fns = []
    for rule in ordering_rules:
        rule_fns.append(get_rule_fn(rule))
    
    valid_updates: list[list[int]] = []
    for update in updates:
        invalid_update = False
        for fn in rule_fns:
            if not fn(update):
                invalid_update = True
                break

        if invalid_update:
            continue

        valid_updates.append(update)

    sum = 0
    for u in valid_updates:
        sum += get_mid_value(u)

    print(sum)
    
if __name__ == '__main__':
    main()