import heapq
from itertools import repeat


def parse_input():
    INPUT = "input.txt"
    with open(INPUT) as file:
        return [int(c) for c in file.readline().strip("\n")]


def solve():
    disk_map = parse_input()

    blocks: list[int | str] = []
    heaps: list[list[int]] = [[] for _ in range(10)]

    # parse
    is_file_space = True
    id = 0
    for block in disk_map:
        c = id if is_file_space else "."
        if c == ".":
            heaps[block].append(len(blocks))
        blocks.extend([b for b in repeat(c, block)])
        id = id if not is_file_space else id + 1
        is_file_space = not is_file_space

    i = len(blocks) - 1
    while i >= 0:
        if blocks[i] == ".":
            i -= 1
            continue

        id = blocks[i]
        width = 0

        while i >= 0 and blocks[i] == id:
            width += 1
            i -= 1

        # Get min index from min heap
        heap_width = 0
        leftmost_free_i = 10**100
        for w, h in enumerate(heaps[width:]):
            if not len(h):
                continue
            if h[0] < leftmost_free_i:
                heap_width = w + width
                leftmost_free_i = h[0]

        if not heap_width:
            continue

        if leftmost_free_i > i:
            continue

        leftmost_free_i = heapq.heappop(heaps[heap_width])

        for j in range(width):
            blocks[leftmost_free_i + j] = id
            blocks[i + j + 1] = "."

        # Store new index for free space if any
        heapq.heappush(heaps[heap_width - width], leftmost_free_i + width)

    # checksum
    checksum = 0
    for index, block in enumerate(blocks):
        if block != ".":
            checksum += index * int(block)
    print(checksum)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
