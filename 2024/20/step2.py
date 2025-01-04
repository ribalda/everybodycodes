import sys
from math import inf
from collections import deque


def navigate(world, start, dir, path):
    hmap = {".": -1, "-": -2, "+": +1, "A": -1, "B": -1, "C": -1, "S": -1}
    time = 0
    todo = deque([(time, start, dir, 0, 0)])
    out = []

    visited = dict()
    while todo:
        time, pos, dir, meters, len_path = todo.popleft()
        if pos == start and len_path > 1:
            if meters > 0:
                return time
            continue

        new_time = time + 1
        for mov in 1, -1j, 1j:
            new_dir = dir * mov
            new_pos = pos + new_dir

            if new_pos not in world:
                continue
            v = world[new_pos]

            if v in ("A", "B", "C", "S"):
                if v != path[len_path]:
                    continue
                new_len_path = len_path + 1
            else:
                new_len_path = len_path

            new_meters = meters + hmap[v]

            idx = (new_pos, new_dir, len_path)
            if idx not in visited:
                visited[idx] = -inf

            if visited[idx] >= new_meters:
                continue
            visited[idx] = new_meters

            todo.append((new_time, new_pos, new_dir, new_meters, new_len_path))
    return out


world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, v in enumerate(line.strip()):
        pos = complex(x, y)
        if v == "S":
            start = pos
        if v == "#":
            continue
        world[pos] = v

print("Part 2:", navigate(world, start, 1, ("A", "B", "C", "S")))
