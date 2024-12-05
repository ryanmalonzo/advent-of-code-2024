from collections import defaultdict
from graphlib import TopologicalSorter


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


def filter_ordering_rules(
    ordering_rules: list[list[str]], update: list[str]
) -> list[list[str]]:
    return [rule for rule in ordering_rules if rule[0] in update and rule[1] in update]


if __name__ == "__main__":
    ordering_rules, updates = parse_file()
    total_middle_number = 0

    for update in updates:
        # Remove any rules that contains a number that is not in the current update
        filtered_ordering_rules = filter_ordering_rules(ordering_rules, update)

        # For each number, build the list of its predecessors
        predecessors = defaultdict(set)
        for rule in filtered_ordering_rules:
            predecessors[rule[1]].add(rule[0])

        # Build the directed acyclic graph from the predecessors
        ts = TopologicalSorter(predecessors)
        ordered_update = [*ts.static_order()]

        if ordered_update == update:
            total_middle_number += int(update[len(update) // 2])

    print(total_middle_number)
