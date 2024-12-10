def parse_input():
    INPUT = "input.txt"
    with open(INPUT) as file:
        arr = []
        t = []
        for i, line in enumerate(file.read().splitlines()):
            curr = [int(c) for c in line]
            arr.append(curr)
            for j, c in enumerate(curr):
                if c == 0:
                    t.append((i, j))
        return arr, t


def scan(
    topographic_map: list[list[int]],
    x: int,
    y: int,
    height: int,
    reached: set[tuple[int, int]],
) -> None:
    if height == 9:
        reached.add((x, y))

    bounds = []
    for z, a in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if (
            z >= 0
            and a >= 0
            and z < len(topographic_map)
            and a < len(topographic_map[0])
            and topographic_map[z][a] == height + 1
        ):
            bounds.append((z, a))

    if not len(bounds):
        return

    for z, a in bounds:
        scan(topographic_map, z, a, height + 1, reached)


def solve():
    topographic_map, trailheads = parse_input()
    sum_scores = 0
    for x, y in trailheads:
        reached: set[tuple[int, int]] = set()
        scan(topographic_map, x, y, 0, reached)
        sum_scores += len(reached)
    print(sum_scores)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
