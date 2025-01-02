import sys


def potions(creatures, groups):
    out = 0
    val = {"A": 0, "B": 1, "C": 3, "D": 5}
    for i in range(0, len(creatures), groups):
        group = creatures[i : i + groups]
        for m in group:
            if m not in val:
                continue
            out += val[m]
            nx = group.count("x")
            out += max(0, groups - nx - 1)
    return out


line = sys.stdin.readline().strip()

for i in range(1, 4):
    print(f"Part {i}: {potions(line, i)}")
