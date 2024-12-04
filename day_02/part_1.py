def parse_file() -> list[list[int]]:
    reports: list[list[int]] = []

    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            report: list[int] = [int(x) for x in line.split(" ")]
            reports.append(report)

    return reports


def check_pairs(report: list[int], a: int, index_a: int) -> bool:
    index_b = index_a + 1

    if index_b == len(report):
        return True

    b = report[index_b]
    c = b - a

    if not (c >= 1 and c <= 3):
        return False

    return check_pairs(report, b, index_b)


def is_safe(report: list[int]) -> bool:
    # The levels are either all increasing or all decreasing.
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return False

    # Any two adjacent levels differ by at least one and at most three.
    report.sort()
    if not check_pairs(report, report[0], 0):
        return False

    return True


if __name__ == "__main__":
    reports = parse_file()
    safe_reports = [report for report in reports if is_safe(report)]
    print(len(safe_reports))
