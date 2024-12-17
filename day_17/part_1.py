import re


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


def process(output: list[str], program: list[int], pointer: int) -> None:
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
        output.append(str(out(operand)))
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
    a, b, c, program = parse_input()
    output: list[str] = []

    while pointer < len(program):
        process(output, program, pointer)

    print(",".join(output))


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve()
    print("--- %s seconds ---" % (time.time() - start_time))
