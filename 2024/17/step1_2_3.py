import sys
from math import inf, prod


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def distance_star(constelation, star):
    dist = inf
    for c in constelation:
        dist = min(distance(c, star), dist)
    return dist


def inc_constelation(constelation, stars, max_size):
    close_star = None
    dist = inf
    for s in stars:
        d = distance_star(constelation, s)
        if d >= max_size:
            continue
        if d < dist:
            close_star = s
            dist = d
    if not close_star:
        return None
    constelation.add(close_star)
    stars.remove(close_star)
    return dist


def constelation_size(stars, max_size):
    constelation = set()
    constelation.add(stars.pop())
    out = 1
    while stars:
        n = inc_constelation(constelation, stars, max_size)
        if not n:
            return out
        out += n + 1

    return out


def constelations_n_max(stars, max_size):
    out = []
    while stars:
        out.append(constelation_size(stars, max_size))
    return out


stars = set()
for x, line in enumerate(sys.stdin.readlines()):
    for y, v in enumerate(line.strip()):
        if v == "*":
            stars.add((x, y))

print("Step 1,2:", constelation_size(stars.copy(), inf))

cons_sizes = constelations_n_max(stars, 6)
cons_sizes = sorted(cons_sizes, reverse=True)[:3]
print("Step 3:", prod(cons_sizes))
