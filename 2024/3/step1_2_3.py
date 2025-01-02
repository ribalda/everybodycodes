import sys


def neir_hor_ver(pos):
    for x in 1j, -1j, 1, -1:
        yield pos + x


def neir_diag(pos):
    for x in 1, -1, 0:
        for y in 1, -1, 0:
            if (x, y) != (0, 0):
                yield pos + complex(x, y)


def dig(world, depth, neir_func):
    do_dig = False
    for w in world:
        if world[w] != depth - 1:
            continue
        neir = neir_func(w)
        for n in neir:
            if n not in world or world[n] < depth - 1:
                break
        else:
            do_dig = True
            world[w] = depth

    return do_dig


def calc_sand(world, neir_func):
    world = world.copy()
    depth = 2
    while dig(world, depth, neir_func):
        depth += 1

    return sum(world.values())


world = dict()
for i, line in enumerate(sys.stdin.readlines()):
    for j, v in enumerate(line.strip()):
        world[complex(i, j)] = 1 if v == "#" else 0


print("Step 1, 2:", calc_sand(world, neir_hor_ver))
print("Step 3:", calc_sand(world, neir_diag))
