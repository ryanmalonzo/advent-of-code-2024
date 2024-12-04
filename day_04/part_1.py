def parse_file() -> list[list[str]]:
    grid = []

    with open("input.txt") as file:
        lines = file.readlines()

        for line in lines:
            grid.append([c for c in line])

    return grid


if __name__ == "__main__":
    grid = parse_file()
    word = "XMAS"
    word_reverse = word[::-1]

    word_count = 0

    # Search horizontally
    for row in grid:
        word_count += "".join(row).count(word)
        word_count += "".join(row).count(word_reverse)

    # Search vertically by transposing the grid
    for column in zip(*grid):
        word_count += "".join(column).count(word)
        word_count += "".join(column).count(word_reverse)

    # Search diagonally
    # https://stackoverflow.com/a/23069625
    height, width = len(grid), len(grid[0])

    diagonals = [
        [
            grid[height - 1 - q][p - q]
            for q in range(min(p, height - 1), max(0, p - width + 1) - 1, -1)
        ]
        for p in range(height + width - 1)
    ]

    for diagonal in diagonals:
        word_count += "".join(diagonal).count(word)
        word_count += "".join(diagonal).count(word_reverse)

    antidiagonals = [
        [grid[p - q][q] for q in range(max(p - height + 1, 0), min(p + 1, width))]
        for p in range(height + width - 1)
    ]

    for antidiagonal in antidiagonals:
        word_count += "".join(antidiagonal).count(word)
        word_count += "".join(antidiagonal).count(word_reverse)

    print(word_count)
