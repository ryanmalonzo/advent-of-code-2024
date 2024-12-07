from copy import deepcopy
from itertools import product


def parse_file():
    equations = []

    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.split(": ")
            result = int(numbers[0])
            operands = [int(number) for number in numbers[1].strip("\n").split(" ")]
            equations.append((result, operands))

    return equations


def calculate(operands, combination):
    op = deepcopy(operands)
    acc = op.pop(0)

    for operator in combination:
        if operator == "+":
            acc += op.pop(0)
        elif operator == "*":
            acc *= op.pop(0)

    return acc


if __name__ == "__main__":
    equations = parse_file()
    operators = ["+", "*"]

    # Sum of all solved equation results
    total_calibration_result = 0

    for result, operands in equations:
        # Get all possible combinations of operators
        combinations = list(product(operators, repeat=len(operands) - 1))

        for combination in combinations:
            combination_result = calculate(operands, combination)

            if combination_result == result:
                total_calibration_result += result
                break

    print(total_calibration_result)
