import sys


def get_world(lines):
    out = dict()
    for x, line in enumerate(lines):
        for y, v in enumerate(line.strip()):
            out[complex(x, y)] = int(v)
    return out


def ignite(world, starts):
    todo = starts
    burnt = set()

    while todo:
        pos = todo.pop()
        for step in complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1):
            new_pos = pos + step
            if new_pos not in world:
                continue
            if world[new_pos] > world[pos]:
                continue
            if new_pos in burnt or new_pos in todo:
                continue
            todo.add(new_pos)
        burnt.add(pos)
    return burnt


def find_best_burnt(world):
    candidates = set(world.keys())
    burnt_out = list()
    while candidates:
        c = candidates.pop()
        burnt = ignite(world, set([c]))
        burnt_out += [burnt]
        candidates -= burnt
    return max(burnt_out, key=len)


def burn_best(world, steps):
    out = 0
    world = world.copy()
    for _ in range(steps):
        burnt = find_best_burnt(world)
        out += len(burnt)
        world = {key: value for key, value in world.items() if key not in burnt}
    return out


world = get_world(sys.stdin.readlines())

print("Step 1:", len(ignite(world, set([complex(0, 0)]))))

corner = max(world.keys(), key=lambda c: (c.real, c.imag))
print("Step 2:", len(ignite(world, set([complex(0, 0), corner]))))

print("Step 3:", burn_best(world, 3))
