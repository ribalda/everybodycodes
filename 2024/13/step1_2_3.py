import sys
import heapq
from math import inf


def calc_min_distance(world, start, end):
    dummy = 0
    dist = 0
    visited = set([start])
    todo = [(dist, dummy, start, visited)]
    distance = {start: 0}
    while todo:
        t = heapq.heappop(todo)
        dist, _, pos, visited = t
        if pos in end:
            return dist

        for inc in 1j, -1j, 1, -1:
            new_pos = pos + inc
            if new_pos in visited:
                continue
            if new_pos not in world:
                continue
            d1 = (world[new_pos] - world[pos]) % 10
            d2 = (world[pos] - world[new_pos]) % 10
            new_dist = dist + min(d1, d2) + 1
            if new_pos not in distance:
                distance[new_pos] = inf
            if distance[new_pos] < new_dist:
                continue
            distance[new_pos] = new_dist
            dummy += 1
            new_visited = visited.copy()
            new_visited.add(new_pos)
            t = (new_dist, dummy, new_pos, new_visited)
            heapq.heappush(todo, t)

    return None


end = set()
world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, v in enumerate(line.strip()):
        pos = complex(x, y)
        if v in ("#", " "):
            continue
        if v == "E":
            start = pos
            v = "0"
        if v == "S":
            end.add(pos)
            v = "0"
        world[pos] = int(v)

print("Part 1,2,3:", calc_min_distance(world, start, end))
