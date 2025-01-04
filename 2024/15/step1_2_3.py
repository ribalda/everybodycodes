import sys
from collections import deque


def find_path(world, plants, start):
    visited = set([(start, ())])
    todo = deque([(0, start, ())])
    while todo:
        d, p, pl = todo.popleft()
        if p == start and len(pl) == len(plants):
            return d
        for inc in 1j, -1j, 1, -1:
            new_p = p + inc
            if new_p not in world:
                continue
            v = world[new_p]
            new_pl = pl
            if v.isalpha() and v not in new_pl:
                new_pl = tuple(sorted(list(set(list(new_pl) + [v]))))
            new_visited = (new_p, new_pl)
            if new_visited in visited:
                continue
            visited.add(new_visited)
            todo.append((d + 1, new_p, new_pl))

    return None


world = dict()
start = None
plants = set()
for x, line in enumerate(sys.stdin.readlines()):
    for y, v in enumerate(line.strip()):
        p = complex(x, y)
        if v in ("#", "~"):
            continue
        if v == "." and not start:
            start = p
        if v.isalpha():
            plants.add(v)

        world[p] = v

print("Part 1,2,3:", find_path(world, plants, start))
