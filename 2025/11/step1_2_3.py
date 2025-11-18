import sys
from itertools import pairwise


def phaseNone(ducks):
    return phaseNone, ducks


def phase1(ducks):
    done = True
    for i in range(len(ducks) - 1):
        if ducks[i + 1] < ducks[i]:
            ducks[i + 1] += 1
            ducks[i] -= 1
            done = False
    if done:
        return phase2(ducks)
    return phase1, ducks


def phase2(ducks):
    done = True
    for i in range(len(ducks) - 1):
        if ducks[i + 1] > ducks[i]:
            ducks[i] += 1
            ducks[i + 1] -= 1
            done = False

    if done:
        return phaseNone(ducks)
    return phase2, ducks


def ducks_crc(ducks):
    return sum([(i + 1) * v for i, v in enumerate(ducks)])


def ducks_cycle(ducks, steps):
    ducks = ducks.copy()
    phase = phase1
    for _ in range(steps):
        phase, ducks = phase(ducks)
    return ducks_crc(ducks)


def ducks_settle(ducks, endphase=phaseNone):
    ducks = ducks.copy()
    phase = phase1
    out = 0
    while phase != endphase:
        out += 1
        phase, ducks = phase(ducks)
    return out - 1


def ducks_settle_fast(ducks):

    # Calculate steps with old method
    steps = ducks_settle(ducks, phase2)

    # Move with fast... not good for calculating steps
    ducks = ducks.copy()
    done = False
    while not done:
        done = True
        for a, b in pairwise(range(len(ducks))):
            if ducks[a] > ducks[b]:
                diff_2 = (ducks[a] - ducks[b] + 1) // 2
                ducks[b] += diff_2
                ducks[a] -= diff_2
                done = False

    done = False
    movs = [0] * len(ducks)
    while not done:
        done = True
        for a, b in pairwise(range(len(ducks))):
            if ducks[a] < ducks[b]:
                diff_2 = (ducks[b] - ducks[a] + 1) // 2
                ducks[b] -= diff_2
                ducks[a] += diff_2
                movs[a] += diff_2
                done = False

    steps += max(movs)
    return steps


ducks = list(map(int, sys.stdin.readlines()))


print("Step 1:", ducks_cycle(ducks, 10))
print("Step 3:", ducks_settle_fast(ducks))
print("Step 2:", ducks_settle(ducks))
