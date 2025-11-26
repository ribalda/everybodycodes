import sys
from heapq import *


def get_world(lines):
    world = dict()
    volc = None
    st = None
    for x, line in enumerate(lines):
        for y, v in enumerate(line.strip()):
            p = complex(x, y)
            if v == "@":
                volc = p
                v = 0
            if v == "S":
                st = p
                v = 0
            world[p] = int(v)
    return volc, st, world


def blast_area(size, offset=complex(0, 0)):
    out = set()
    for x in range(size + 1):
        for y in range(size + 1):
            if x * x + y * y <= size * size:
                out.add(complex(x, y) + offset)
                out.add(complex(-x, y) + offset)
                out.add(complex(x, -y) + offset)
                out.add(complex(-x, -y) + offset)
    return out


def calc_blast(pos, size, world):
    out = 0
    for p in blast_area(size):
        out += world.get(pos + p, 0)

    return out


def biggest_ring(pos, world):
    last_blast = 0
    biggest_diff = 0
    biggest_step = None

    step = 0
    while True:
        step += 1
        new_blast = calc_blast(pos, step, world)
        if new_blast == last_blast:
            return biggest_diff * biggest_step

        diff = new_blast - last_blast
        if diff > biggest_diff:
            biggest_diff = diff
            biggest_step = step
        last_blast = new_blast


def print_distances(vis, world):
    print("")
    for i in range(100):
        if complex(i, 0) not in world:
            continue
        out = ""
        for j in range(100):
            if complex(i, j) not in world:
                continue
            kk = vis.pop(complex(i, j), -1)
            out += "{0:4d}".format(kk)
        print(out)


def shortest_circle(v, s, world, area):
    todo = []

    burnt = blast_area(area, v)
    max_dist = 30 * (area + 1)

    visited_dist = [dict(), dict()]
    has_crossed = 0
    dist = 0
    dummy = 0

    heappush(todo, (dist, dummy, has_crossed, s))
    while todo:
        dist, _, has_crossed, pos = heappop(todo)
        if has_crossed and pos == s:
            # print_distances(visited_dist[0], world)
            # print_distances(visited_dist[1], world)
            return dist

        if pos in visited_dist[has_crossed] and visited_dist[has_crossed][pos] <= dist:
            continue

        visited_dist[has_crossed][pos] = dist
        for d in complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1):
            new_pos = pos + d
            if new_pos not in world or new_pos in burnt:
                continue
            new_dist = dist + world[new_pos]
            if new_dist >= max_dist:
                continue

            if new_pos.imag == v.imag and new_pos.real > v.real:
                if pos.imag > v.imag and not has_crossed:
                    continue

            if pos.imag == v.imag and pos.real > v.real:
                if new_pos.imag < v.imag and has_crossed:
                    continue
                if new_pos.imag > v.imag and not has_crossed:
                    dummy += 1
                    heappush(todo, (new_dist, dummy, 1, new_pos))

            dummy += 1
            heappush(todo, (new_dist, dummy, has_crossed, new_pos))

    return None


def step3(v, s, world):
    i = 0
    while True:
        out = shortest_circle(v, s, world, i)
        if out != None:
            # print(i, out)
            return i * out
        i += 1


v, st, world = get_world(sys.stdin.readlines())

print("Step 1:", calc_blast(v, 10, world))
print("Step 2:", biggest_ring(v, world))

if not st:
    sys.exit(0)

print("Step 3:", step3(v, st, world))
