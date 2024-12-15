from collections import deque


def parse_input():
    INPUT = "input.txt"
    with open(INPUT) as file:
        lines = file.read().splitlines()
    sep = lines.index("")
    warehouse: list[list[str]] = []
    for line in lines[:sep]:
        l = "".join(c * 2 if c != "@" else "@." for c in line)
        l = l.replace("OO", "[]")
        warehouse.append([c for c in l])
    directions = list("".join(lines[sep + 1 :]))
    return warehouse, directions[::-1]


def find_robot(warehouse: list[list[str]]) -> tuple[int, int]:
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "@":
                return (y, x)
    raise Exception("Robot not found")


DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


boxes: list[tuple[int, int, str]] = []
visted: list[list[bool]] = []


def adjacent(y: int, x: int, dy: int, dx: int) -> tuple[int, int]:
    return (y + dy, x + dx)


def is_valid(warehouse: list[list[str]], y: int, x: int) -> bool:
    return y >= 0 and x >= 0 and y < len(warehouse) and x < len(warehouse[0])


def bfs(warehouse: list[list[str]], y: int, x: int, dy: int, dx: int) -> None:
    global boxes
    global visited

    def enqueue(y: int, x: int) -> None:
        q.append((y, x))
        visited[y][x] = True
        boxes.append((y, x, warehouse[y][x]))

    def handle_pair(y: int, x: int, direction: int) -> None:
        paired_x = x + direction
        enqueue(y, paired_x)

    q: deque[tuple[int, int]] = deque()
    enqueue(y, x)

    if warehouse[y][x] == "[":
        handle_pair(y, x, 1)
    else:
        handle_pair(y, x, -1)

    while q:
        y, x = q.popleft()
        a, z = adjacent(y, x, dy, dx)
        if (
            is_valid(warehouse, a, z)
            and not visited[a][z]
            and warehouse[a][z] in ["[", "]"]
        ):
            enqueue(a, z)

            if warehouse[a][z] == "[":
                handle_pair(a, z, 1)
            else:
                handle_pair(a, z, -1)


def move(
    warehouse: list[list[str]],
    robot: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    global boxes
    global visited

    ry, rx = robot
    dy, dx = DIRECTIONS[direction]

    y, x = ry + dy, rx + dx

    if warehouse[y][x] == "#":
        return robot

    if warehouse[y][x] in ["[", "]"]:
        # bfs to find all adjacent boxes
        boxes = []
        visited = [[False] * len(warehouse[0]) for _ in range(len(warehouse))]
        bfs(warehouse, y, x, dy, dx)

        # check if we can push
        for a, z, _ in boxes:
            if warehouse[a + dy][z + dx] == "#":
                return robot

        # move boxes
        for a, z, _ in boxes:
            warehouse[a][z] = "."
        for a, z, symbol in boxes:
            warehouse[a + dy][z + dx] = symbol

    # move robot
    warehouse[ry][rx] = "."
    warehouse[y][x] = "@"

    return ry + dy, rx + dx


def solve():
    warehouse, directions = parse_input()
    robot = find_robot(warehouse)

    while len(directions):
        direction = directions.pop()
        robot = move(warehouse, robot, direction)

    sum_coordinates = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "[":
                sum_coordinates += 100 * y + x
    print(sum_coordinates)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
