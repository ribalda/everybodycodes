import sys
from itertools import permutations


def calc_power(device, track, steps):
    total = 0
    p = 10
    for i in range(steps):
        op = device[i % len(device)]
        tr = track[i % len(track)]
        if tr == "+":
            p += 1
        elif tr == "-":
            p -= 1
        elif op == "+":
            p += 1
        elif op == "-":
            p -= 1
        elif op == "=":
            p = p
        p = max(0, p)
        total += p

    return total


def parse_terrain(terr):
    world = dict()
    for i, line in enumerate(terrain.splitlines()):
        for j, v in enumerate(line.strip()):
            if v != " ":
                world[complex(i, j)] = v
            if v == "S":
                p = complex(i, j)
    visited = set()
    out = ""
    while True:
        for i in 1j, -1j, 1, -1:
            new_p = p + i
            if new_p not in visited and new_p in world:
                p = new_p
                break
        visited.add(p)
        out += world[p]
        if world[p] == "S":
            return out


terrain = """S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-"""

devices = dict()
for line in sys.stdin.readlines():
    name, ops = line.strip().split(":")
    devices[name] = ops.split(",")

terrain = parse_terrain(terrain)
a_power = calc_power(devices["A"], terrain, 2024 * len(terrain))
out = 0
for t in set(permutations("+++++---===")):
    t = list(t)
    st = "".join(t)
    t_power = calc_power(t, terrain, 2024 * len(terrain))
    if t_power > a_power:
        out += 1

print("Part 3:", out)
