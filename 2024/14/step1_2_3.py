import sys
from collections import deque
from math import inf


def get_plant(inst):
    points = []
    pos = (0, 0, 0)
    for i in inst:
        d = i[0]
        n = int(i[1:])
        if d == "U":
            for _ in range(n):
                pos = pos[0] + 1, pos[1], pos[2]
                points.append(pos)
        elif d == "D":
            for _ in range(n):
                pos = pos[0] - 1, pos[1], pos[2]
                points.append(pos)
        elif d == "L":
            for _ in range(n):
                pos = pos[0], pos[1] - 1, pos[2]
                points.append(pos)
        elif d == "R":
            for _ in range(n):
                pos = pos[0], pos[1] + 1, pos[2]
                points.append(pos)
        elif d == "F":
            for _ in range(n):
                pos = pos[0], pos[1], pos[2] + 1
                points.append(pos)
        elif d == "B":
            for _ in range(n):
                pos = pos[0], pos[1], pos[2] - 1
                points.append(pos)
        else:
            print(Error)

    return points


def get_next(p):
    yield p[0] + 1, p[1], p[2]
    yield p[0] - 1, p[1], p[2]
    yield p[0], p[1] + 1, p[2]
    yield p[0], p[1] - 1, p[2]
    yield p[0], p[1], p[2] + 1
    yield p[0], p[1], p[2] - 1


def distance(plant, p1, p2):
    visited = set([p1])
    todo = deque([(0, p1)])
    while todo:
        t = todo.popleft()
        d, p = t
        if p == p2:
            return d
        for new_p in get_next(p):
            if new_p not in plant:
                continue
            if new_p in visited:
                continue
            visited.add(new_p)
            todo.append((d + 1, new_p))


def get_best_point(plant, leafs):
    murk_min = inf
    candidates = [p for p in plant if p[1] == 0 and p[2] == 0]
    for c in candidates:
        murk = 0
        for l in leafs:
            murk += distance(plant, l, c)
        murk_min = min(murk, murk_min)

    return murk_min


plants = []
for line in sys.stdin.readlines():
    insts = line.strip().split(",")
    plants.append(get_plant(insts))

print("Part 1:", max([x[0] for x in plants[0]]))

full_plant = set()
for p in plants:
    full_plant |= set(p)
print("Part 2:", len(full_plant))

leafs = [p[-1] for p in plants]
print("Part 3:", get_best_point(full_plant, leafs))
