import functools
from collections import defaultdict


def parse_input() -> dict[int, int]:
    INPUT = "input.txt"
    with open(INPUT) as file:
        stones = defaultdict(lambda: 0)
        for line in file.read().splitlines():
            for s in line.split(" "):
                stones[int(s)] += 1
        return stones


@functools.cache
def compute(stone_str, stone_len):
    return int(stone_str[: stone_len // 2]), int(stone_str[stone_len // 2 :])


def blink(stones: dict[int, int], count: int, until: int) -> dict[int, int]:
    if count > until:
        return stones

    new_stones = defaultdict(lambda: 0)

    for k, v in stones.items():
        if k == 0:
            new_stones[1] += v
            continue

        stone_str = str(k)
        stone_len = len(stone_str)
        if stone_len % 2 == 0:
            left, right = compute(stone_str, stone_len)
            new_stones[left] += v
            new_stones[right] += v
            continue

        res = k * 2024
        new_stones[res] += v

    return blink(new_stones, count + 1, until)


def solve():
    stones = parse_input()
    stones = blink(stones, 1, 75)
    total = sum([v for v in stones.values()])
    print(total)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
