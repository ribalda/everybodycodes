import sys
from functools import cache


@cache
def base_len(level):
    return 2 * level - 1


@cache
def height_len(level, nullp, acolytes):
    if level == 1:
        return 1
    return (height_len(level - 1, nullp, acolytes) * nullp) % acolytes


@cache
def n_blocks(height, nullp, acolytes):
    if height == 1:
        return 1

    o = base_len(height) * height_len(height, nullp, acolytes)
    o += n_blocks(height - 1, nullp, acolytes)
    return o


nullp = int(sys.stdin.readline())
if nullp == 3:
    acolytes = 5
    blocks = 50
else:
    acolytes = 1111
    blocks = 20240000

full_blocks = 0
height = 0
while full_blocks < blocks:
    height += 1
    full_blocks = n_blocks(height, nullp, acolytes)


print("Step 2:", (full_blocks - blocks) * base_len(height))
