def parse_input():
    INPUT = "input.txt"
    with open(INPUT) as file:
        lines = file.read().splitlines()
    patterns: set[str] = set(lines[0].split(", "))
    designs: list[str] = []
    for line in lines[2:]:
        designs.append(line)
    return patterns, designs


def lookup(patterns: set[str], design: str) -> bool:
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # empty design is valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and design[j:i] in patterns:
                dp[i] = True
                break

    return dp[-1]


def solve():
    patterns, designs = parse_input()
    possible = 0
    for design in designs:
        if lookup(patterns, design):
            possible += 1
    print(possible)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
