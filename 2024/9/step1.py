import sys


def decompose(ball):
    stamps = [10, 5, 3, 1]
    out = 0
    for s in stamps:
        out += ball // s
        ball = ball % s
    return out


balls = map(int, sys.stdin.readlines())
out = sum(map(decompose, balls))
print("Part 1:", out)
