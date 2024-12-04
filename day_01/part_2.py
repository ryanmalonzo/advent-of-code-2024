def parse_file() -> tuple[list[int], list[int]]:
    left_locations: list[int] = []
    right_locations: list[int] = []

    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            locations: list[int] = [int(x) for x in line.split("   ")]
            left_locations.append(locations[0])
            right_locations.append(locations[1])

    return left_locations, right_locations


if __name__ == "__main__":
    left_locations, right_locations = parse_file()

    total_similarity_score = 0
    for i in range(len(left_locations)):
        total_similarity_score += (
            right_locations.count(left_locations[i]) * left_locations[i]
        )

    print(total_similarity_score)
