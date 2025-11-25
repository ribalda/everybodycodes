import sys
from math import prod


def block_sum(size, pattern):
    out = 0
    for p in pattern:
        out += size // p

    return out


def patern_from_blocks(blocks):
    out = []
    blocks = list(blocks)
    for i in range(len(blocks)):
        if not blocks[i]:
            continue
        out.append(i + 1)
        for j in range(i, len(blocks), i + 1):
            blocks[j] -= 1
    return tuple(out)


def find_length(blocks, pattern):
    left, right = 0, blocks
    while (right - left) > 1:
        center = (left + right) // 2
        b = block_sum(center, pattern)
        if b < blocks:
            left = center
        else:
            right = center
    return left


pattern = tuple(map(int, sys.stdin.readline().split(",")))
print("Step 1:", block_sum(90, pattern))

blocks = pattern
pattern = patern_from_blocks(blocks)
print("Step 2:", prod(pattern))

print("Step 3:", find_length(202520252025000, pattern))
