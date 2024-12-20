import copy
import heapq
import itertools
from collections import defaultdict


def parse_input():
    INPUT = "input.txt"
    grid: list[list[str]] = []
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)
    with open(INPUT) as file:
        lines = file.read().splitlines()
        for y, line in enumerate(lines):
            curr: list[str] = []
            for x, c in enumerate(line):
                curr.append(c)
                if c == "S":
                    start = (y, x)
                elif c == "E":
                    end = (y, x)
            grid.append(curr)
    return grid, start, end


def get_adjacent_cells(
    grid: list[list[str]], position: tuple[int, int], walls: bool = False
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
        if (
            0 <= y < len(grid)
            and 0 <= x < len(grid[0])
            and (grid[a][z] == "#" if walls else grid[a][z] != "#")
        ):
            res.append((a, z))
    return res


def dijkstra(
    grid: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    queue: list[tuple[int, tuple[int, int]]] = []
    heapq.heappush(queue, (0, start))

    distances: dict[tuple[int, int], int] = defaultdict(lambda: 10**10)
    distances[start] = 0

    predecessors: dict[tuple[int, int], tuple[int, int] | None] = {}
    predecessors[start] = None

    while queue:
        current_distance, current_position = heapq.heappop(queue)

        if current_position == end:
            path: list[tuple[int, int]] = []
            while current_position:
                path.append(current_position)
                current_position = predecessors[current_position]
            return distances, path[::-1]

        for y, x in get_adjacent_cells(grid, current_position):
            new_distance = current_distance + 1
            if new_distance < distances[(y, x)]:
                distances[(y, x)] = new_distance
                predecessors[(y, x)] = current_position
                heapq.heappush(queue, (new_distance, (y, x)))

    return {}, []


def manhattan_neighbours(y: int, x: int, r: int):
    for dy, dx in itertools.product(range(-r, r + 1), repeat=2):
        if abs(dy) + abs(dx) <= r:
            yield ((y + dy, x + dx), abs(dy) + abs(dx))


def solve():
    grid, start, end = parse_input()
    distances, _ = dijkstra(grid, start, end)
    frozen_distances = copy.deepcopy(distances)
    cheats: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for y, x in frozen_distances.keys():
        for (a, z), r in manhattan_neighbours(y, x, 20):
            if (a, z) in frozen_distances.keys() and (
                distances[(a, z)] - (distances[(y, x)] + r) >= 100
            ):
                cheats.add(((y, x), (a, z)))
    print(len(cheats))


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
