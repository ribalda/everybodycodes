import sys
from collections import deque
from math import inf


def visit(world, start, palms, max_time_sum):
    visited = start
    visited_palms = set()
    times = []
    time = 0
    todo = deque([])
    for s in start:
        todo.append((0, s))

    while todo:
        time, pos = todo.popleft()
        if sum(times) > max_time_sum:
            return None
        if world[pos] == "P":
            times.append(time)
            visited_palms.add(pos)
            if visited_palms == palms:
                return times
        for inc in 1j, -1j, 1, -1:
            new_pos = pos + inc
            if new_pos not in world:
                continue
            if new_pos in visited:
                continue
            visited.add(new_pos)
            todo.append((time + 1, new_pos))
    return None


def best_point(world, palms):
    valid_starts = set([x for x in world if world[x] == "."])
    best_sum = inf
    for s in valid_starts:
        times = visit(world, set([s]), palms, best_sum)
        if not times:
            continue
        best_sum = min(best_sum, sum(times))
    return best_sum


world = dict()
palms = set()
start = set()
for x, line in enumerate(sys.stdin.readlines()):
    line = line.strip()
    for y, val in enumerate(line):
        if val == "#":
            continue
        pos = complex(x, y)
        if y == 0 or y == len(line) - 1:
            start.add(pos)
        if val == "P":
            palms.add(pos)
        world[pos] = val

times = visit(world, start, palms, inf)
if times:
    print("Part 1,2:", max(times))

print("Part 3:", best_point(world, palms))
