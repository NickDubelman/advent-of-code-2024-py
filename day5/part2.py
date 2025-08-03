from part1 import load_input, get_rule_fn, get_mid_value

def main():
    ordering_rules, updates = load_input()
    
    # Sort the ordering_rules by increasing {first_num}
    # This isn't needed but optimizes how quickly the updates can be fixed
    # To see the effect, you can comment it out and re-run
    ordering_rules = sorted(ordering_rules, key=lambda rule: rule[0])

    # Accumulate a list of functions that take an update and return a bool
    rule_fns = []
    for rule in ordering_rules:
        rule_fns.append(get_rule_fn(rule))
    
    iterations_required_to_fix: list[int] = []
    fixed_updates: list[list[int]] = []
    for update in updates:
        needed_fix = False
        iteration_count = 0

        # We will keep looping until the update is fixed
        while True:
            iteration_count += 1
            is_valid = True
            for i, fn in enumerate(rule_fns):
                if fn(update):
                    continue
                
                needed_fix = True
                is_valid = False
                rule = ordering_rules[i]

                first_num = rule[0]
                second_num = rule[1]
                second_num_idx = update.index(second_num)

                # Put {first_num} in the index right before {second_num}
                update = (
                    update[:second_num_idx]
                    + [first_num, second_num]
                    + [num for num in update[second_num_idx + 1:] if num != first_num]
                )

            if is_valid:
                if needed_fix:
                    iterations_required_to_fix.append(iteration_count)
                    fixed_updates.append(update)

                # Update has been fixed, break out of infinite while
                break


    avg_iterations = sum(iterations_required_to_fix) / len(iterations_required_to_fix)
    print(f'Average num of iterations required to fix update: {avg_iterations:.2f}')

    result = sum([get_mid_value(update) for update in fixed_updates])
    print(result)
        
    
if __name__ == '__main__':
    main()