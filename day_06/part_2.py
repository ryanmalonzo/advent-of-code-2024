from copy import deepcopy


def parse_file() -> list[list[str]]:
    with open("input.txt") as file:
        # with open("test.txt") as file:
        lab_map = []

        lines = file.readlines()
        for line in lines:
            lab_map.append([character.strip("\n") for character in line])

        return lab_map


def get_guard_position(lab_map):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] == "^":
                return i, j


def out_of_bounds(lab_map, position):
    x = position[0]
    y = position[1]
    return x < 0 or y < 0 or x >= len(lab_map) or y >= len(lab_map[0])


def get_next_position(current_position, direction):
    return current_position[0] + direction[0], current_position[1] + direction[1]


def get_next_direction(current_direction):
    if current_direction == (-1, 0):
        return 0, 1
    if current_direction == (0, 1):
        return 1, 0
    if current_direction == (1, 0):
        return 0, -1
    return -1, 0


def get_nominal_path(lab_map, current_position, current_direction):
    visited_positions: set[tuple[int, int]] = set()

    while not out_of_bounds(lab_map, current_position):
        x, y = get_next_position(current_position, current_direction)
        next_position = x, y

        if out_of_bounds(lab_map, next_position):
            break

        if lab_map[x][y] != "#":
            current_position = next_position
            visited_positions.add(current_position)
        else:
            # Turn 90 degrees right
            current_direction = get_next_direction(current_direction)

    return visited_positions


if __name__ == "__main__":
    lab_map = parse_file()
    initial_guard_position = get_guard_position(lab_map)

    loop_positions = set()

    # The obstacles can only be placed where the guard normally goes
    # So we can speed up the process by doing a normal run first
    nominal_path_positions = get_nominal_path(lab_map, initial_guard_position, (-1, 0))

    for position in nominal_path_positions:
        i = position[0]
        j = position[1]

        if (i, j) == initial_guard_position:
            continue

        current_lab_map = deepcopy(lab_map)
        current_lab_map[i][j] = "#"

        current_position = initial_guard_position
        current_direction = -1, 0

        visited_positions = set()
        visited_positions.add((current_position, current_direction))

        while not out_of_bounds(current_lab_map, current_position):
            x, y = get_next_position(current_position, current_direction)
            next_position = x, y

            # No loop
            if out_of_bounds(current_lab_map, next_position):
                break

            if current_lab_map[x][y] != "#":
                current_position = next_position

                # Loop
                if (current_position, current_direction) in visited_positions and (
                    current_position,
                    current_direction,
                ) != initial_guard_position:
                    loop_positions.add((i, j))
                    break

                visited_positions.add((current_position, current_direction))

            else:
                # Turn 90 degrees right
                current_direction = get_next_direction(current_direction)

    print(len(loop_positions))
