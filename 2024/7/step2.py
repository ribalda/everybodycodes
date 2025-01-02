import sys


def calc_power(devices, track, steps):
    out = dict()
    for d in devices:
        total = 0
        p = 10
        for i in range(steps):
            op = devices[d][i % len(devices[d])]
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
            total += p
        out[d] = total
    return out


def parse_terrain(terr):
    terr = terr.splitlines()
    out = terr[0].strip()[1:]
    for j in range(1, len(terr) - 1):
        out += terr[j].strip()[-1]
    out += terr[-1].strip()[::-1]
    for j in range(len(terr) - 2, -1, -1):
        out += terr[j].strip()[0]
    return out


terrain_small = """S+===
-   +
=+=-+"""
terrain_big = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""

devices = dict()
for line in sys.stdin.readlines():
    name, ops = line.strip().split(":")
    devices[name] = ops.split(",")


terrain = terrain_small if len(devices) == 4 else terrain_big
terrain = parse_terrain(terrain)


power = calc_power(devices, terrain, 10 * len(terrain))
ranking = "".join(
    x[1] for x in sorted(((v, k) for k, v in power.items()), reverse=True)
)
print("Step 2:", ranking)
