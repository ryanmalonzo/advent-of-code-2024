import re


def parse_input():
    INPUT = "input.txt"
    robots: list[tuple[tuple[int, int], tuple[int, int]]] = []
    with open(INPUT) as file:
        lines = file.read().splitlines()
        for line in lines:
            matches = re.findall(r"(-?\d+)", line)
            robot = (
                (int(matches[0]), int(matches[1])),
                (int(matches[2]), int(matches[3])),
            )
            robots.append(robot)
    return robots


WIDTH, HEIGHT = 101, 103


def move(robots, i) -> None:
    position, velocity = robots[i]
    new_x = (position[0] + velocity[0]) % WIDTH
    new_y = (position[1] + velocity[1]) % HEIGHT
    robots[i] = ((new_x, new_y), velocity)


def solve():
    robots = parse_input()
    seconds = 1
    while True:
        for i in range(len(robots)):
            move(robots, i)
        if len(set(pos for pos, _ in robots)) == len(robots):
            break
        seconds += 1
    print(seconds)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
