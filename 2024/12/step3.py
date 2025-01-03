import sys
from math import inf


def inc_hitting_pos(hitting_pos, power, time, pos):
    if pos not in hitting_pos:
        hitting_pos[pos] = []
    hitting_pos[pos].append((power, time))


def calc_hitting_pos(hitting_pos, init_pos, mult, max_time):
    for power in range(max_time):
        time = 0
        pos = init_pos
        inc_hitting_pos(hitting_pos, power * mult, time, pos)
        for _ in range(power):
            time += 1
            pos = (pos[0] + 1, pos[1] + 1)
            inc_hitting_pos(hitting_pos, power * mult, time, pos)
        for _ in range(power):
            time += 1
            pos = (pos[0], pos[1] + 1)
            inc_hitting_pos(hitting_pos, power * mult, time, pos)
        while pos[0] > 0:
            time += 1
            pos = (pos[0] - 1, pos[1] + 1)
            inc_hitting_pos(hitting_pos, power * mult, time, pos)


def best_hitting(hitting_pos, m):
    time = 0
    while m[0] >= 0:
        if m in hitting_pos:
            best = inf
            for p, t in hitting_pos[m]:
                if time >= t:
                    best = min(best, p)
            if best != inf:
                return best
        m = (m[0] - 1, m[1] - 1)
        time += 1
    return 0


rockets = {1: (0, 0), 2: (1, 0), 3: (2, 0)}
meteors = list()

for line in sys.stdin.readlines():
    meteors.append(tuple(map(int, reversed(line.split(" ")))))

max_time = max([x[0] for x in meteors])

hitting_pos = dict()
for r in rockets:
    calc_hitting_pos(hitting_pos, rockets[r], r, max_time)

out = 0
for m in meteors:
    out += best_hitting(hitting_pos, m)

print("Step 3:", out)
