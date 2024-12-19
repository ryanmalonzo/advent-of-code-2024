import heapq
from collections import defaultdict


def parse_input():
    INPUT = "input.txt"
    LENGTH = 70 + 1
    MAX = 1024
    grid: list[list[str]] = [["."] * 71 for _ in range(LENGTH)]
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (LENGTH - 1, LENGTH - 1)
    i = 0
    with open(INPUT) as file:
        lines = file.read().splitlines()
        while i < MAX:
            split = lines[i].split(",")
            x = int(split[0])
            y = int(split[1])
            grid[y][x] = "#"
            i += 1
    return grid, start, end


def get_adjacent_cells(
    grid: list[list[str]], position: tuple[int, int]
) -> list[tuple[int, int]]:
    y, x = position
    res: list[tuple[int, int]] = []
    for (
        a,
        z,
    ) in [
        (y - 1, x),
        (y, x + 1),
        (y + 1, x),
        (y, x - 1),
    ]:
        if 0 <= a < len(grid) and 0 <= z < len(grid[0]) and grid[a][z] != "#":
            res.append((a, z))
    return res


def dijkstra(
    grid: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> int:
    queue: list[tuple[int, tuple[int, int]]] = []
    heapq.heappush(queue, (0, start))

    distances: dict[tuple[int, int], int] = defaultdict(lambda: 10**10)
    distances[start] = 0

    while len(queue):
        current_distance, current_position = heapq.heappop(queue)

        if current_position == end:
            return current_distance

        for y, x in get_adjacent_cells(grid, current_position):
            new_distance = current_distance + 1
            # found better distance
            if new_distance < distances[(y, x)]:
                distances[(y, x)] = new_distance
                heapq.heappush(queue, (new_distance, (y, x)))

    return -1


def solve():
    grid, start, end = parse_input()
    print(dijkstra(grid, start, end))


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
