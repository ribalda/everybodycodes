import sys
from functools import cache


@cache
def nparts(num):
    stamps = reversed(
        [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    )
    if num == 0:
        return 0
    o = num
    for s in stamps:
        if num >= s:
            o = min(o, 1 + nparts(num - s))
    return o


def mindiv(num):
    o = num
    mid = num // 2
    for i in range(0, 100 // 2 + 1):
        a = mid - i
        b = num - a
        if abs(a - b) > 100:
            continue
        o = min(o, nparts(a) + nparts(b))

    return o


sys.setrecursionlimit(10000)
balls = map(int, sys.stdin.readlines())
out = sum(map(mindiv, balls))
print("Part 3:", out)
