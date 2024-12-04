def parse_file() -> list[list[str]]:
    grid = []

    with open("input.txt") as file:
        lines = file.readlines()

        for line in lines:
            grid.append([c for c in line])

    return grid


def get_cell(grid: list[list[str]], i: int, j: int) -> str:
    if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[i])):
        return "."
    return grid[i][j]


def is_word(word: str, cells: list[str]) -> bool:
    return "".join(cells) == word or "".join(cells)[::-1] == word


if __name__ == "__main__":
    grid = parse_file()
    word = "MAS"

    x_mas_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cell = get_cell(grid, i, j)

            if cell == "A":
                diagonal_cells = []
                antidiagonal_cells = []

                diagonal_cells.append(get_cell(grid, i - 1, j - 1))
                diagonal_cells.append(cell)
                diagonal_cells.append(get_cell(grid, i + 1, j + 1))

                antidiagonal_cells.append(get_cell(grid, i - 1, j + 1))
                antidiagonal_cells.append(cell)
                antidiagonal_cells.append(get_cell(grid, i + 1, j - 1))

                if is_word(word, diagonal_cells) and is_word(word, antidiagonal_cells):
                    x_mas_count += 1

    print(x_mas_count)
