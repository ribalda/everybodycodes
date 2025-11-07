from math import ceil, floor
import sys


def get_gear(line):
    return tuple(map(int, line.split("|")))


def get_factor(gears):
    last = gears[0][-1]
    mult = 1
    for g in gears[1:]:
        mult *= last / g[0]
        last = g[-1]
    return mult


gears = tuple(map(get_gear, sys.stdin.readlines()))
factor = get_factor(gears)

print("Step 1:", floor(factor * 2025))
print("Step 2:", ceil(10000000000000 / factor))
print("Step 3:", floor(factor * 100))
