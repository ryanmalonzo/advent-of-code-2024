import re


def parse_file() -> list:
    all_matches = []

    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            matches = re.findall(r"mul\((\d+),(\d+)\)", line)
            if matches:
                all_matches.extend((int(a), int(b)) for a, b in matches)

    return all_matches


if __name__ == "__main__":
    all_matches = parse_file()

    total = 0

    for x, y in all_matches:
        total += x * y

    print(total)
