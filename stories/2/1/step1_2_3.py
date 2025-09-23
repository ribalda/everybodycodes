import sys
from functools import cache
from itertools import permutations


def end_pos(slots, ins, pos):
    x = (pos - 1) * 2
    y = 0
    i = 0
    if x >= len(slots[0]):
        return 0

    while y < len(slots):
        if slots[y][x] == "*":
            if ins[i] == "L":
                x = x - 1
            else:
                x = x + 1
            i += 1

        if x < 0:
            x += 2
        if x >= len(slots[y]):
            x -= 2
        y += 1

    # print(pos, x // 2 + 1)
    return x // 2 + 1


@cache
def calc_val(slots, ins, pos):
    return max(0, 2 * end_pos(slots, ins, pos) - pos)


slots, instructions = sys.stdin.read().split("\n\n")
slots = tuple(map(str.strip, slots.splitlines()))
instructions = tuple(map(str.strip, instructions.splitlines()))


val = 0
for idx, ins in enumerate(instructions):
    val += calc_val(slots, ins, idx + 1)

print("Step 1: ", val)

val = 0
startpos = tuple(range(1, len(slots[0]) // 2 + 2))
for idx, ins in enumerate(instructions):
    v = 0
    for i in startpos:
        v = max(v, calc_val(slots, ins, i))
    # print(v)
    val += v
print("Step 2: ", val)

min_val = float("inf")
max_val = 0
for permu in permutations(startpos, len(instructions)):
    v = 0
    for i, c in enumerate(permu):
        v += calc_val(slots, instructions[i], c)
    min_val = min(min_val, v)
    max_val = max(max_val, v)
print("Step 3: ", min_val, max_val)
