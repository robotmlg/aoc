import re
from collections import defaultdict

def parse(file="input.txt"):
    rules = defaultdict(list)
    updates = []

    with open(file, "r") as f:
        for line in f:
            if match := re.match(r"(\d+)\|(\d+)", line):
                key, val = int(match.group(1)), int(match.group(2))
                rules[key].append(val)
            elif line.strip():
                updates.append([int(n) for n in line.split(",")])

    return rules, updates


def evaluate_rules(rules, update):
    for i in range(len(update)):
        page = update[i]
        page_rules = rules.get(page, [])
        for rule in page_rules:
            try:
                target_index = update.index(rule)
            except ValueError:
                continue
            if target_index > i:
                continue
            return False  # this rule errored
    return True


def fix_update(rules, update):
    if len(update) == 1:
        return update
    # only fix the first element, we'll fix the rest recursively
    valid = False
    while not valid:
        page = update[0]
        page_rules = rules.get(page, [])
        for rule in page_rules:
            try:
                target_index = update.index(rule)
            except ValueError:
                continue
            if target_index > 0:
                # back check all the rules for the target number
                target_rules = rules.get(rule, [])
                for target_rule in target_rules:
                    try:
                        target_target_index = update.index(target_rule)
                    except ValueError:
                        continue
                    if target_target_index > target_index:
                        continue
                    # this rule is not met, swap the elements and start over
                    update[target_target_index], update[target_index] = update[target_index], update[target_target_index]
                    break
            # this rule is not met, swap the elements and start over
            update[0], update[target_index] = update[target_index], update[0]
            break
        if evaluate_rules({page: page_rules}, update):
            valid = True

    return [update[0]] + fix_update(rules, update[1:])


def part1(rules, updates):
    return sum([
        update[(len(update) - 1) // 2]
        for update in updates
        if evaluate_rules(rules, update)
    ])


def part2(rules, updates):
    invalid_updates = [list(update) for update in updates if not evaluate_rules(rules, update)]
    fixed_updates = [fix_update(rules, update) for update in invalid_updates]
    return sum([
        update[(len(update) - 1) // 2]
        for update in fixed_updates
    ])


rules, updates = parse()
print(part1(rules, updates))
print(part2(rules, updates))

