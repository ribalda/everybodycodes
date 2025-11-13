import sys
from itertools import pairwise


def calc_knots(p, pairs, with_same=False):
    out = 0
    left_nails = range(p[0] + 1, p[1])
    for a, b in pairs:
        if with_same:
            if a == p[0] and b == p[1]:
                out += 1
                continue
        if (a in p) or (b in p):
            continue
        if (a in left_nails) != (b in left_nails):
            out += 1

    return out


def step3(pairs, nails):
    max_out = 0
    for a in range(1, nails + 1):
        for b in range(a + 1, nails + 1):
            max_out = max(calc_knots((a, b), pairs, True), max_out)
    return max_out


def step2(pairs):
    out = 0
    for i, p in enumerate(pairs):
        out += calc_knots(p, pairs[:i])
    return out


def step1(pairs, nails):
    return sum([(b == (a + nails // 2)) for (a, b) in pairs])


numbers = tuple(map(int, sys.stdin.readline().split(",")))
if len(numbers) >= 1000:
    nails = 256
elif len(numbers) >= 100:
    nails = 32
else:
    nails = 8

pairs = tuple([(min(p), max(p)) for p in pairwise(numbers)])

print("Step 1:", step1(pairs, nails))
print("Step 2:", step2(pairs))
print("Step 3:", step3(pairs, nails))
