import sys
from heapq import *


def get_world(lines):
    world = dict()
    for line in lines:
        x, y, l = map(int, line.split(","))
        if x not in world:
            world[x] = list()
        world[x].append(range(y, y + l))

    return world


def shortest_path_slow(world):
    target = max(world.keys()) + 1
    todo = []
    heappush(todo, (0, 0, 0))
    visited = dict()
    while todo:
        flaps, xpos, ypos = heappop(todo)
        if (xpos, ypos) in visited:
            if visited[(xpos, ypos)] <= flaps:
                continue
        visited[(xpos, ypos)] = flaps

        if xpos == target:
            return flaps

        for dof in True, False:
            new_xpos = xpos + 1
            if dof:
                new_ypos = ypos + 1
                new_flaps = flaps + 1
            else:
                new_ypos = ypos - 1
                new_flaps = flaps
            if new_ypos < 0:
                continue
            if new_xpos not in world:
                heappush(todo, (new_flaps, new_xpos, new_ypos))
                continue
            for hole_range in world[new_xpos]:
                if new_ypos in hole_range:
                    heappush(todo, (new_flaps, new_xpos, new_ypos))


def shortest_path(world):
    barriers = list(world.keys()) + [0]
    barriers.sort()
    barriers = tuple(barriers)
    todo = []
    heappush(todo, (0, 0, 0))
    visited = dict()
    while todo:
        flaps, xpos, ypos = heappop(todo)
        if (xpos, ypos) in visited:
            if visited[(xpos, ypos)] <= flaps:
                continue
        visited[(xpos, ypos)] = flaps

        if xpos == len(barriers) - 1:
            return flaps

        new_xpos = xpos + 1
        distance = barriers[new_xpos] - barriers[xpos]

        valid_range = range(ypos - distance, ypos + distance + 1, 2)
        for hole_range in world[barriers[new_xpos]]:
            if (
                valid_range.start >= hole_range.stop
                or hole_range.start >= valid_range.stop
            ):
                continue
            for new_ypos in hole_range:
                if new_ypos not in valid_range:
                    continue
                n_flaps = (new_ypos - ypos + distance) // 2
                heappush(todo, (flaps + n_flaps, new_xpos, new_ypos))


world = get_world(sys.stdin.readlines())
print("Step 1,2,3:", shortest_path(world))
# print("Step 1,2,3:", shortest_path_slow(world))
