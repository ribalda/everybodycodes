import sys
from math import inf
from collections import deque


def navigate(world, start, dir, max_time):
    hmap = {".": -1, "-": -2, "+": +1, "S": -1}
    time = 0
    todo = deque([(time, start, dir, 0)])
    max_meters = -inf

    visited = dict()
    while todo:
        time, pos, dir, meters = todo.popleft()
        if time == max_time:
            max_meters = max(meters, max_meters)
            continue

        new_time = time + 1
        for mov in 1, -1j, 1j:
            new_dir = dir * mov
            new_pos = pos + new_dir

            if new_pos not in world:
                continue
            v = world[new_pos]

            new_meters = meters + hmap[v]

            idx = (new_pos, new_dir)
            if idx not in visited:
                visited[idx] = -inf

            if visited[idx] >= new_meters:
                continue
            visited[idx] = new_meters

            todo.append((new_time, new_pos, new_dir, new_meters))
    return max_meters


world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, v in enumerate(line.strip()):
        pos = complex(x, y)
        if v == "S":
            start = pos
        if v == "#":
            continue
        world[pos] = v

print("Part 1:", 1000 + navigate(world, start, 1, 100))
