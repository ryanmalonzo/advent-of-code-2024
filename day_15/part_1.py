def parse_input():
    INPUT = "input.txt"
    with open(INPUT) as file:
        lines = file.read().splitlines()
    sep = lines.index("")
    warehouse = [list(line) for line in lines[:sep]]
    directions = list("".join(lines[sep + 1 :]))
    return warehouse, directions[::-1]


def find_robot(warehouse: list[list[str]]) -> tuple[int, int]:
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == "@":
                return (y, x)
    raise Exception("Robot not found")


DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def move(
    warehouse: list[list[str]],
    robot: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    ry, rx = robot
    dy, dx = DIRECTIONS[direction]
    boxes: list[tuple[int, int]] = []

    free_space = False
    y, x = ry + dy, rx + dx
    while warehouse[y][x] != "#":
        if warehouse[y][x] == "O":
            boxes.append((y, x))
        elif warehouse[y][x] == ".":
            free_space = True
            break
        y, x = y + dy, x + dx

    if not free_space:
        return robot

    # move boxes
    for y, x in boxes:
        warehouse[y + dy][x + dx] = "O"

    # move robot
    warehouse[ry][rx] = "."
    warehouse[ry + dy][rx + dx] = "@"

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
            if warehouse[y][x] == "O":
                sum_coordinates += 100 * y + x
    print(sum_coordinates)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
