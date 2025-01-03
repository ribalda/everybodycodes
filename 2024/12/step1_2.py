import sys


def shoot_power(target, rocket):
    hdist = target[1] - rocket[1]
    for power in range(hdist):
        pos = rocket
        for _ in range(power):
            pos = (pos[0] + 1, pos[1] + 1)
            if pos == target:
                return power
        for _ in range(power):
            pos = (pos[0], pos[1] + 1)
            if pos == target:
                return power
        while pos[0] > 0:
            pos = (pos[0] - 1, pos[1] + 1)
            if pos == target:
                return power

    return None


targets = list()
rockets = dict()
lines = sys.stdin.readlines()
height = len(lines)
for x, line in enumerate(lines):
    for y, v in enumerate(line.strip()):
        pos = (height - x - 1, y)
        if v in (".", "="):
            continue
        if v == "T":
            targets.append((pos, 1))
        elif v == "H":
            targets.append((pos, 2))
        else:
            rockets[v] = pos

mult = {"A": 1, "B": 2, "C": 3}
out = 0
for t in targets:
    for r in rockets:
        power = shoot_power(t[0], rockets[r])
        if power:
            out += mult[r] * power * t[1]

print("Step 1:", out)
