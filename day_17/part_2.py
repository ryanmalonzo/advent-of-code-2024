import heapq
import re
from collections import defaultdict


def parse_input():
    INPUT = "input.txt"
    registers: list[int] = [0] * 3
    with open(INPUT) as file:
        lines = file.read().splitlines()
    i = 0
    while i < len(registers):
        registers[i] = int(re.findall(r"(\d+)", lines[i])[0])
        i += 1
    program = [int(x) for x in lines[-1].split("Program: ")[1].split(",")]
    return registers[0], registers[1], registers[2], program


def combo(operand: int) -> int:
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    return c


a: int = 0
b: int = 0
c: int = 0
pointer: int = 0


def adv(operand: int) -> None:
    global a
    global pointer
    a = a // 2 ** combo(operand)
    pointer += 2


def bxl(operand: int) -> None:
    global b
    global pointer
    b = b ^ operand
    pointer += 2


def bst(operand: int) -> None:
    global b
    global pointer
    b = combo(operand) % 8
    pointer += 2


def jnz(operand: int) -> None:
    global a
    global pointer
    if a == 0:
        pointer += 2
        return
    pointer = operand


def bxc(operand: int) -> None:
    global b
    global c
    global pointer
    b = b ^ c
    pointer += 2


def out(operand: int) -> int:
    global pointer
    pointer += 2
    return combo(operand) % 8


def bdv(operand: int) -> None:
    global a
    global b
    global pointer
    b = a // (2 ** combo(operand))
    pointer += 2


def cdv(operand: int) -> None:
    global a
    global c
    global pointer
    c = a // 2 ** combo(operand)
    pointer += 2


def process(output: list[int], program: list[int], pointer: int) -> None:
    opcode = program[pointer]
    operand = program[pointer + 1]
    if opcode == 0:
        return adv(operand)
    if opcode == 1:
        return bxl(operand)
    if opcode == 2:
        return bst(operand)
    if opcode == 3:
        return jnz(operand)
    if opcode == 4:
        return bxc(operand)
    if opcode == 5:
        output.append(out(operand))
        return
    if opcode == 6:
        return bdv(operand)
    return cdv(operand)


def solve():
    global a
    global b
    global c
    global pointer
    # program = list of instructions = list of opcodes
    _, b, c, program = parse_input()
    output: list[int] = []

    i = 1
    start_a = 0
    cur_a = 0
    # i => list of valid A values
    valid_a: dict[int, list[int]] = defaultdict(list)
    tested_a: set[int] = set()

    # dfs + backtracking for digits from end to start
    # shifting by 3 bits every time we find a good value
    while output != program:
        # input()
        output = []
        pointer = 0

        # try A with current value
        a = cur_a
        while pointer < len(program):
            process(output, program, pointer)

        if output == program:
            break

        if output == program[-i:]:
            if cur_a not in tested_a:
                valid_a[i].append(cur_a)
                valid_a[i].sort()

        # if we finished checking for numbers and couldn't find a match, backtrack
        if not len(valid_a[i]) and start_a + 7 == cur_a:
            i -= 1
            while not len(valid_a[i]):
                i -= 1
            cur_a = heapq.heappop(valid_a[i])
            tested_a.add(cur_a)
            cur_a *= 8
            start_a = cur_a
            i += 1
            continue

        # if we finished checking for numbers and we have at least one match, go to next digit
        if len(valid_a[i]) and start_a + 7 == cur_a:
            cur_a = heapq.heappop(valid_a[i])
            tested_a.add(cur_a)
            cur_a *= 8
            start_a = cur_a
            i += 1
            continue

        cur_a += 1

    print(cur_a)


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
