from collections import defaultdict
from itertools import combinations


def parse_file():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    antennas = defaultdict(list)
    map_x, map_y = (len(lines), len(lines[0]))

    for i in range(map_x):
        for j in range(map_y):
            if lines[i][j] != ".":
                antennas[lines[i][j]].append((i, j))

    return (map_x, map_y), antennas


def add_antinode(map_dimensions, antinodes, coords):
    x, y = coords
    if x >= 0 and x < map_dimensions[0] and y >= 0 and y < map_dimensions[1]:
        antinodes.add(coords)


if __name__ == "__main__":
    map_dimensions, antennas = parse_file()
    antennas = {k: v for k, v in antennas.items() if len(v) > 1}
    pairs = {antenna: list(combinations(antennas[antenna], 2)) for antenna in antennas}

    unique_antinodes = set()
    compare = lambda a, b: (a > b) - (a < b)
    for _, coordinates in pairs.items():
        for (x1, y1), (x2, y2) in coordinates:
            x_diff = abs(x1 - x2)
            y_diff = abs(y1 - y2)
            add_antinode(
                map_dimensions,
                unique_antinodes,
                (x1 + x_diff * compare(x1, x2), y1 + y_diff * compare(y1, y2)),
            )
            add_antinode(
                map_dimensions,
                unique_antinodes,
                (x2 + x_diff * compare(x2, x1), y2 + y_diff * compare(y2, y1)),
            )

    print(len(unique_antinodes))
