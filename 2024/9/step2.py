import sys
from functools import cache


@cache
def nparts(num):
    stamps = reversed([1, 3, 5, 10, 15, 16, 20, 24, 25, 30])
    if num == 0:
        return 0
    o = num
    for s in stamps:
        if num >= s:
            o = min(o, 1 + nparts(num - s))
    return o


sys.setrecursionlimit(10000)
balls = map(int, sys.stdin.readlines())
out = sum(map(nparts, balls))
print("Part 2:", out)
