import sys


def parse_line(line):
    id, faces, seed = line.split()
    id = int(id[:-1])
    faces = tuple(map(int, faces[7:-1].split(",")))
    seed = int(seed[5:])
    # id pos roll pulse faces seed race_idx
    return id, 0, 0, seed, faces, seed, 0


def calc_spin_pulse(roll_number, pulse, seed):
    spin = roll_number * pulse
    pulse = pulse + spin
    pulse = pulse % seed
    pulse = pulse + 1 + roll_number + seed
    return spin, pulse


def roll(dice, race):
    id, pos, roll, pulse, faces, seed, race_idx = dice
    roll += 1
    spin, pulse = calc_spin_pulse(roll, pulse, seed)
    pos = (pos + spin) % len(faces)
    if faces[pos] == race[race_idx]:
        race_idx += 1
    return (id, pos, roll, pulse, faces, seed, race_idx)


dices, race = sys.stdin.read().split("\n\n")
dices = tuple(map(parse_line, dices.splitlines()))
race = tuple(map(int, race.strip()))

out_order = []
while dices:
    out_dices = []
    for d in dices:
        d = roll(d, race)
        if d[6] == len(race):
            out_order += [d[0]]
            continue
        out_dices += [d]
    dices = tuple(out_dices)

print("Step 2:", ",".join(map(str, out_order)))
