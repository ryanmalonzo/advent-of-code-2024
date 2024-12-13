import re


def parse_input() -> list[tuple[list[int], list[int]]]:
    INPUT = "input.txt"
    systems = []
    with open(INPUT) as file:
        lines = list(file.read().splitlines())
        i = 0
        while i < len(lines):
            if lines[i] == "":
                i += 1
                continue
            eq1 = [0, 0, 0]
            eq2 = [0, 0, 0]
            matches = re.findall(r"(\d+)", lines[i])
            eq1[0], eq2[0] = int(matches[0]), int(matches[1])
            matches = re.findall(r"(\d+)", lines[i + 1])
            eq1[1], eq2[1] = int(matches[0]), int(matches[1])
            matches = re.findall(r"(\d+)", lines[i + 2])
            eq1[2], eq2[2] = 10000000000000 + int(matches[0]), 10000000000000 + int(
                matches[1]
            )
            systems.append((eq1, eq2))
            i += 3
    return systems


def cramer(e1: list[int], e2: list[int]) -> tuple[int, int]:
    determinant = e1[0] * e2[1] - e1[1] * e2[0]
    if not determinant:
        return 0, 0
    a = (e1[2] * e2[1] - e1[1] * e2[2]) / determinant
    b = (e1[0] * e2[2] - e1[2] * e2[0]) / determinant
    if not a.is_integer() or not b.is_integer():
        return 0, 0
    return int(a), int(b)


def solve():
    A_TOKENS = 3
    B_TOKENS = 1
    sum_tokens = 0
    systems = parse_input()
    for e1, e2 in systems:
        a, b = cramer(e1, e2)
        sum_tokens += A_TOKENS * a + B_TOKENS * b
    print(sum_tokens)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
