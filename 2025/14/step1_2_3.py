import sys


def get_world(lines):
    out = dict()
    for x, line in enumerate(lines):
        for y, v in enumerate(line.strip()):
            out[complex(x, y)] = v
    return out


def get_diagonals(world, w):
    for x in complex(1, 1), complex(1, -1), complex(-1, 1), complex(-1, -1):
        p = w + x
        if p in world:
            yield (world[p])


def step(world):
    out = dict()
    for w in world:
        n_on = sum([c == "#" for c in get_diagonals(world, w)])
        if world[w] == "#":
            if n_on % 2:
                out[w] = "#"
            else:
                out[w] = "."
        else:
            if n_on % 2:
                out[w] = "."
            else:
                out[w] = "#"
    return out


def n_on(world, steps):
    out = 0
    for _ in range(steps):
        world = step(world)
        out += sum([1 for w in world.values() if w == "#"])
    return out


def empty_world(first, last):
    out = dict()
    for i in range(first, last + 1):
        for j in range(first, last + 1):
            out[complex(i, j)] = "."
    return out


def n_pattern_cycle(min, max, pattern, steps):
    world = empty_world(min, max)
    out = 0
    visited = dict()
    partial_out = dict()
    for i in range(steps):
        world = step(world)
        on = frozenset([w for w in world.keys() if world[w] == "#"])
        for p in pattern:
            if pattern[p] != world[p]:
                break
        else:
            out += len(on)
        partial_out[i] = out
        if on in visited:
            missing_steps = steps - i
            cycle_size = i - visited[on]
            cycles = missing_steps // cycle_size

            out += cycles * (partial_out[i] - partial_out[visited[on]])
            left = missing_steps % cycle_size
            out += partial_out[visited[on] + left] - partial_out[visited[on]]
            return out
        visited[on] = i
    return out


world = get_world(sys.stdin.readlines())


print("Step 1:", n_on(world, 10))
print("Step 2:", n_on(world, 2025))
print("Step 3:", n_pattern_cycle(-13, 33 - 13, world, 1000000000))
