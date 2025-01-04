import sys
from copy import deepcopy
import re


def get_around(pos):
    x, y = pos
    yield x - 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1
    yield x + 1, y
    yield x + 1, y - 1
    yield x, y - 1


def rotate(message, pos, inc):
    around = []
    for x, y in get_around(pos):
        around.append(message[x][y])
    for i, (x, y) in enumerate(get_around(pos)):
        message[x][y] = around[(i + inc) % len(around)]


def operate(message, instructions):
    ins2inc = {"L": 1, "R": -1}
    i = 0
    for x in range(1, len(message) - 1):
        for y in range(1, len(message[0]) - 1):
            rotate(message, (x, y), ins2inc[instructions[i % len(instructions)]])
            i += 1


def calc_rotate(message, instructions):
    rots = []
    for x in range(len(message)):
        line = []
        for y in range(len(message[0])):
            line.append((x, y))
        rots.append(line)

    operate(rots, instructions)
    return rots


def operate_rotate(message, rots):
    out = []
    for rot in rots:
        line = []
        for x, y in rot:
            line.append(message[x][y])
        out.append(line)
    return out


def get_txt(message):
    return "\n".join(["".join(line) for line in message])


def calc_multirot(rot):
    out = [rot]
    for _ in range(31):
        rot = operate_rotate(rot, rot)
        out.append(rot)
    return out


def operate_multirot(message, multirot, steps):
    for i, rot in enumerate(multirot):
        if steps & (1 << i):
            message = operate_rotate(message, rot)
    return message


instructions, message = sys.stdin.read().split("\n\n")
instructions = tuple(instructions)
message = list(map(lambda x: list(x.strip()), message.splitlines()))

rots = calc_rotate(message, instructions)
message = operate_rotate(message, rots)
print("Part 1:")
print(get_txt(message), "\n")


multirot = calc_multirot(rots)
message = operate_multirot(message, multirot, 100 - 1)
print("Part 2:")
print(get_txt(message), "\n")


message = operate_multirot(message, multirot, 1048576000 - 100)
print("Part 3:")
print(get_txt(message), "\n")
