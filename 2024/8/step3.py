import sys
from functools import cache


@cache
def base_len(level):
    return 2 * level - 1


@cache
def height_len(level, nullp, acolytes):
    if level == 1:
        return 1
    return ((height_len(level - 1, nullp, acolytes) * nullp) % acolytes) + acolytes


@cache
def n_blocks(height, nullp, acolytes):
    if height == 1:
        return 1

    o = base_len(height) * height_len(height, nullp, acolytes)
    o += n_blocks(height - 1, nullp, acolytes)
    return o


def removal_blocks(height, nullp, acolytes):
    if height == 1:
        return 0
    h = height_len(height, nullp, acolytes)
    out = 0
    for i in range(height - 1, 1, -1):
        h += height_len(i, nullp, acolytes)
        out += 2 * ((nullp * h * (2 * height - 1)) % acolytes)
    h += height_len(1, nullp, acolytes)
    out += (nullp * h * (2 * height - 1)) % acolytes
    return out


nullp = int(sys.stdin.readline())
if nullp == 2:
    acolytes = 5
    blocks = 160
else:
    acolytes = 10
    blocks = 202400000

full_blocks = 0
height = 0
while full_blocks < blocks:
    height += 1
    full_blocks = n_blocks(height, nullp, acolytes)
    full_blocks -= removal_blocks(height, nullp, acolytes)


print("Step 2:", full_blocks - blocks)
