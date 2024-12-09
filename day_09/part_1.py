from itertools import repeat


def parse_file():
    with open("input.txt") as file:
        return [int(c) for c in file.readline().strip("\n")]


if __name__ == "__main__":
    disk_map = parse_file()

    blocks = []
    is_file_space = True
    id = 0
    for block in disk_map:
        c = id if is_file_space else "."
        blocks.extend([str(b) for b in repeat(c, block)])
        id = id if not is_file_space else id + 1
        is_file_space = not is_file_space

    file_blocks = [(index, b) for index, b in enumerate(blocks) if b != "."]

    for index, block in enumerate(blocks):
        # Check if replacements are over
        remaining = blocks[-index:]
        if remaining.count(".") == len(blocks) - index:
            break

        if blocks[index] == ".":
            fb_index, fb = file_blocks.pop()
            blocks[fb_index] = "."
            blocks[index] = fb

    checksum = 0
    for index, block in enumerate(blocks):
        if block != ".":
            checksum += index * int(block)
    print(checksum)
