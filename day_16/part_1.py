import heapq
from collections import defaultdict
from enum import Enum

MOVE_SCORE = 1
ROTATION_SCORE = 1000


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)


DIRECTIONS = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]


def parse_input():
    INPUT = "input.txt"
    maze: list[list[str]] = []
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
            maze.append(curr)
    return maze, start, end


def move(
    start_direction: Direction,
    target_direction: Direction,
) -> tuple[Direction, int]:
    if start_direction != target_direction:
        start_i = DIRECTIONS.index(start_direction)
        target_i = DIRECTIONS.index(target_direction)

        clockwise_dist = (target_i - start_i) % len(DIRECTIONS)
        counterclockwise_dist = (start_i - target_i) % len(DIRECTIONS)

        rotation_score = ROTATION_SCORE * min(clockwise_dist, counterclockwise_dist)
        return target_direction, MOVE_SCORE + rotation_score

    return target_direction, MOVE_SCORE


def get_adjacent_cells(
    maze: list[list[str]], position: tuple[int, int]
) -> list[tuple[int, int, Direction]]:
    y, x = position
    res: list[tuple[int, int, Direction]] = []
    for a, z, d in [
        (y - 1, x, Direction.NORTH),
        (y, x + 1, Direction.EAST),
        (y + 1, x, Direction.SOUTH),
        (y, x - 1, Direction.WEST),
    ]:
        if 0 <= a < len(maze) and 0 <= z < len(maze[0]) and maze[a][z] != "#":
            res.append((a, z, d))
    return res


def dijkstra(
    maze: list[list[str]],
    start: tuple[int, int],
    end: tuple[int, int],
    direction: Direction,
) -> int:
    queue: list[tuple[int, tuple[int, int], Direction]] = []
    heapq.heappush(queue, (0, start, direction))

    scores: dict[tuple[int, int], int] = defaultdict(lambda: 10**10)
    scores[start] = 0

    while len(queue):
        current_score, current_position, current_direction = heapq.heappop(queue)

        if current_position == end:
            return current_score

        for y, x, d in get_adjacent_cells(maze, current_position):
            next_direction, move_score = move(current_direction, d)
            new_score = current_score + move_score

            # found better score
            if new_score < scores[(y, x)]:
                scores[(y, x)] = new_score
                heapq.heappush(queue, (new_score, (y, x), next_direction))

    return -1


def solve():
    maze, start, end = parse_input()
    initial_direction = Direction.EAST
    print(dijkstra(maze, start, end, initial_direction))


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
