import re


def parse_file() -> list:
    all_matches = []

    with open("input.txt") as file:
        lines = file.readlines()
        pattern = r"mul\((\d+),(\d+)\)|\b(do|don't)\b"

        for line in lines:
            for match in re.finditer(pattern, line):
                if match.group(1) and match.group(2):
                    num1 = int(match.group(1))
                    num2 = int(match.group(2))
                    all_matches.append((num1, num2))
                elif match.group(3) == "do":
                    all_matches.append(True)
                elif match.group(3) == "don't":
                    all_matches.append(False)

        return all_matches


if __name__ == "__main__":
    all_matches = parse_file()

    total = 0

    do_state: bool = True
    for match in all_matches:
        if type(match) == bool:
            do_state = match
        # The do() instruction enables future mul instructions.
        elif do_state:
            x, y = match
            total += x * y

    print(total)
