from collections import defaultdict


def parse_file() -> tuple[list[list[str]], list[list[str]]]:
    with open("input.txt") as file:
        lines = file.readlines()

    # Use carriage return as separator to get the ordering rules and the updates separately
    carriage_return_index = lines.index("\n")

    ordering_rules = lines[:carriage_return_index]
    updates = lines[carriage_return_index + 1 :]

    ordering_rules = [rule.strip("\n").split("|") for rule in ordering_rules]
    updates = [update.strip("\n").split(",") for update in updates]

    return ordering_rules, updates


if __name__ == "__main__":
    ordering_rules, updates = parse_file()

    predecessors = defaultdict(list)
    successors = defaultdict(list)

    for rule in ordering_rules:
        predecessors[rule[1]].append(rule[0])
        successors[rule[0]].append(rule[1])

    total_middle = 0

    for update in updates:
        is_in_order: bool = True

        for i in range(len(update)):
            i_predecessors = update[:i]
            i_successors = update[i + 1 :]

            if any(
                predecessor
                for predecessor in i_predecessors
                if predecessor in successors[update[i]]
            ) or any(
                successor
                for successor in i_successors
                if successor in predecessors[update[i]]
            ):
                is_in_order = False
                break

        if is_in_order:
            total_middle += int(update[(len(update)) // 2])

    print(total_middle)
