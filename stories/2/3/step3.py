import sys


def parse_line(line):
    id, faces, seed = line.split()
    id = int(id[:-1])
    faces = tuple(map(int, faces[7:-1].split(",")))
    seed = int(seed[5:])
    # id pos roll pulse faces seed
    return id, 0, 0, seed, faces, seed


def parse_mapa_line(line):
    return tuple(map(int, line.strip()))


def parse_mapa(inp):
    mapa = tuple(map(parse_mapa_line, inp.splitlines()))
    out = dict()
    for x, line in enumerate(mapa):
        for y, val in enumerate(line):
            out[complex(x, y)] = val
    return out


def get_all_players(mapa):
    out = []
    for pos in mapa:
        out += [(pos, set())]
    return out


def calc_spin_pulse(roll_number, pulse, seed):
    spin = roll_number * pulse
    pulse = pulse + spin
    pulse = pulse % seed
    pulse = pulse + 1 + roll_number + seed
    return spin, pulse


def roll(dice):
    id, pos, roll, pulse, faces, seed = dice
    roll += 1
    spin, pulse = calc_spin_pulse(roll, pulse, seed)
    pos = (pos + spin) % len(faces)
    return (id, pos, roll, pulse, faces, seed)


def debug_map(mapa, reacheable):
    for x in range(1000):
        if complex(x, 0) not in mapa:
            break
        out = ""
        for y in range(1000):
            if complex(x, y) not in mapa:
                break
            if complex(x, y) in reacheable:
                out += str(mapa[complex(x, y)])
            else:
                out += " "
        print(out)


def calc_reacheable(mapa, dice):
    players = get_all_players(mapa)
    reacheable = set()

    while players:
        next_pos = set()
        out_players = []
        dice = roll(dice)
        next_value = dice[4][dice[1]]
        for pos, visited in players:
            if mapa[pos] != next_value:
                reacheable |= visited
                continue
            visited.add(pos)
            for step in (0, -1j, 1j, 1, -1):
                new_pos = pos + step
                if new_pos not in mapa:
                    continue
                if new_pos in next_pos:
                    reacheable |= visited
                    continue
                new_p = (new_pos, visited.copy())
                out_players += [new_p]
                next_pos.add(new_pos)
        players = out_players

    return reacheable


dices, mapa = sys.stdin.read().split("\n\n")
dices = tuple(map(parse_line, dices.splitlines()))
mapa = parse_mapa(mapa)


total_reacheable = set()
for d in dices:
    total_reacheable |= calc_reacheable(mapa, d)

debug_map(mapa, total_reacheable)

print("Step 3:", len(total_reacheable))
