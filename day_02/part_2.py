def parse_file() -> list[list[int]]:
    reports: list[list[int]] = []

    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            report: list[int] = [int(x) for x in line.split(" ")]
            reports.append(report)

    return reports


def is_safe(report: list[int]) -> bool:
    current_order = None

    for index_i, i in enumerate(report):
        index_j = index_i + 1

        if index_j == len(report):
            return True

        j = report[index_j]

        diff = i - j

        # The levels are either all increasing or all decreasing.
        if diff == 0:
            return False

        if diff > 0:
            if current_order == "asc":
                return False
            current_order = "desc"
        if diff < 0:
            if current_order == "desc":
                return False
            current_order = "asc"

        # Any two adjacent levels differ by at least one and at most three.
        abs_diff = abs(diff)
        if not (abs_diff >= 1 and abs_diff <= 3):
            return False

    return True


if __name__ == "__main__":
    reports = parse_file()
    safe_reports = []

    for report in reports:
        # All combinations of the report with one number removed at a time
        combinations = [report[:i] + report[i + 1 :] for i in range(len(report))]
        if any(is_safe(combination) for combination in combinations):
            safe_reports.append(report)

    print(len(safe_reports))
